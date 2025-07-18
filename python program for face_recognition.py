import cv2
import numpy as np
import pandas as pd

# Load Student Database
student_db = pd.read_csv("student_db.csv")

# Load Trained Face Recognizer
recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read("trained_model.yml")

# Load Haar Cascade
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

# Get student names from dataset
student_names = {idx: name for idx, name in enumerate(student_db["Student Name"])}

def recognize_students(image_path, class_name):
    image = cv2.imread(image_path)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)

    recognized_students = []
    
    for (x, y, w, h) in faces:
        face = gray[y:y+h, x:x+w]
        face = cv2.resize(face, (100, 100))

        label, confidence = recognizer.predict(face)
        student_name = student_names.get(label, "Unknown")

        if student_name in student_db[student_db["Class Name"] == class_name]["Student Name"].values:
            recognized_students.append(student_name)

    return recognized_students
