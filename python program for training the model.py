import cv2
import os
import numpy as np
from datetime import datetime
import pandas as pd

# Initialize the LBPH Face Recognizer
recognizer = cv2.face.LBPHFaceRecognizer_create()

# Load Haar Cascade for face detection
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

# Path to student images dataset
dataset_path = "ES"

faces = []
labels = []
student_names = {}  # Store student labels dynamically
label_id = 0

# Process all student images
for filename in os.listdir(dataset_path):
    img_path = os.path.join(dataset_path, filename)

    if not filename.lower().endswith((".jpg", ".jpeg", ".png")):  # Ignore non-image files
        continue

    image = cv2.imread(img_path)

    if image is None:
        print(f"⚠️ Skipping {filename} (Invalid Image)")
        continue

    # Convert to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Detect faces in the image
    detected_faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)

    for (x, y, w, h) in detected_faces:
        face_cropped = gray[y:y+h, x:x+w]  # Crop the detected face
        face_resized = cv2.resize(face_cropped, (100, 100))  # Resize for uniformity

        faces.append(face_resized)
        labels.append(label_id)

    # Extract student name from filename (e.g., "John_Doe_1.jpg" → "John_Doe")
    student_name = os.path.splitext(filename)[0].rsplit("_", 1)[0]  # Remove extra numbering if present
    student_names[label_id] = student_name
    label_id += 1

if len(faces) == 0:
    print("❌ No faces detected. Please check the dataset!")
else:
    # Convert labels to NumPy array
    labels = np.array(labels)

    # Train the recognizer
    recognizer.train(faces, labels)

    # Save trained model
    recognizer.save("trained_model.yml")
    print("✅ Model trained and saved as 'trained_model.yml'")
    print("📌 Student Labels:", student_names)

def recognize_and_update_attendance(image_path):
    image = cv2.imread(image_path)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    detected_faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)

    recognized_students = []

    for (x, y, w, h) in detected_faces:
        face_cropped = gray[y:y+h, x:x+w]
        face_resized = cv2.resize(face_cropped, (100, 100))

        label, confidence = recognizer.predict(face_resized)
        student_name = student_names.get(label, "Unknown")

        print(f"🆔 Recognized: {student_name} | Confidence: {round(confidence, 2)}")

        if student_name != "Unknown":
            recognized_students.append(student_name)

    if recognized_students:
        update_attendance(recognized_students)
    else:
        print("❌ No known student recognized.")

# 📌 Update attendance in Excel
def update_attendance(recognized_students):
    file_name = "attendance.xlsx"
    now = datetime.now()
    timestamp = now.strftime("%Y-%m-%d %H:%M:%S")

    # Load existing attendance file or create new
    if os.path.exists(file_name):
        df = pd.read_excel(file_name)
    else:
        df = pd.DataFrame(columns=["Student Name", "Timestamp"])

    # Add attendance entries
    for student in recognized_students:
        new_entry = {"Student Name": student, "Timestamp": timestamp}
        df = pd.concat([df, pd.DataFrame([new_entry])], ignore_index=True)

    # Save updated attendance file
    df.to_excel(file_name, index=False)
    print("✅ Attendance updated successfully!")

# 📌 Run Recognition
recognize_and_update_attendance("class_image.jpg")


