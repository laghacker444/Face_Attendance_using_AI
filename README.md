# Face_Attendance_using_AI
An automated classroom attendance system using RFID for teacher authentication and CNN-based face recognition for students. It scans faces randomly throughout lectures to ensure presence, improving reliability. Achieves 80% accuracy and 100ms RFID response via Arduino and camera integration.

The system workflow begins with a teacher tapping their RFID card, which activates the system. Subsequently, the camera scans the classroom, identifies student faces using deep learning models such as CNN  and marks their attendance in real-time. Integration with a microcontroller (Arduino) and a camera module allows seamless communication and processing.

The project achieved an average face recognition accuracy of 80% and RFID authentication within 100 milliseconds. Testing under varied lighting and environmental conditions highlighted challenges such as multiple faces per frame and occasional RFID misreads.
Our system ensures reliable, secure, and automated attendance tracking with a potential for broader adoption in educational institutions.

The novelty of our system lies in its continuous and randomized face scanning mechanism. Rather than marking attendance after a single scan, our model scans student faces at random intervals throughout the lecture duration (e.g., a 50-minute class). If a student's face is detected in more than 75% of the scans until a defined threshold (e.g., 30 minutes), the system marks the student as present. This prevents manipulation where students might leave the class early after a single scan, thereby significantly improving reliability

This project demonstrates a significant advancement in educational automation, offering enhanced operational efficiency, improved security, and the potential for large-scale implementation across academic institutions.

Keywords: Face Recognition, RFID, Deep Learning, Embedded System, Attendance Automation, Real-Time Processing

Video link:- https://drive.google.com/file/d/1oWuTftIksRiK967j7-eVYyXec9zvpNro/view?usp=sharing
