import pandas as pd
import os
from datetime import datetime

def update_attendance(students):
    file_name = "attendance.xlsx"
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    if os.path.exists(file_name):
        df = pd.read_excel(file_name)
    else:
        df = pd.DataFrame(columns=["Student Name", "Timestamp"])

    new_entries = pd.DataFrame([{"Student Name": student, "Timestamp": timestamp} for student in students])
    df = pd.concat([df, new_entries], ignore_index=True)

    df.to_excel(file_name, index=False)
    print("✅ Attendance Updated!")
