import face_recognition
import cv2
import numpy as np
import pyttsx3

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)
engine.setProperty("rate", 170)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

# Load the reference face image
reference_face = face_recognition.load_image_file("my.jpg")
reference_encoding = face_recognition.face_encodings(reference_face)[0]

# Open the webcam
video = cv2.VideoCapture(0)

while True:
    speak("Detecting Your Face, Sir")

    # Capture a frame from the webcam
    _, frame = video.read()

    # Resize the frame for faster processing
    resized_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
    resized_frame_rgb = resized_frame[:, :, ::-1]

    # Find face locations and encodings in the frame
    face_locations = face_recognition.face_locations(resized_frame)
    face_encodings = face_recognition.face_encodings(resized_frame_rgb, face_locations)

    for face_encoding in face_encodings:
        # Compare the detected face with the reference face
        face_distance = face_recognition.face_distance([reference_encoding], face_encoding)
        if face_distance[0] < 0.5:  # You can adjust the threshold for face matching
            video.release()
            cv2.destroyAllWindows()
            speak("Face Matched Successfully")
            # You can add more actions or logic here when the face is matched
            exit()

    # Display the frame with face locations
    for (top, right, bottom, left) in face_locations:
        top *= 4
        right *= 4
        bottom *= 4
        left *= 4

        cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)

    cv2.imshow('Face Scan', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

video.release()
cv2.destroyAllWindows()
