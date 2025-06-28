# Import the OpenCV library for computer vision tasks
import cv2

# Load the Haar cascade classifier for face detection
# This file must be present in the OpenCV haarcascades directory
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalcatface.xml')

def detect_face():
    # Open a connection to the default camera (webcam index 0)
    cap = cv2.VideoCapture(0)

    while True:
         # Read a frame from the webcam
        success, img = cap.read()

        # Convert the frame to grayscale for better face detection performance
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        # Detect faces in the grayscale frame
        face = face_cascade.detectMultiScale(gray, 1.1, 4)

        # Draw a green rectangle around each detected face
        for (x, y, w, h) in face:
            cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)

        # Display the frame with detected faces in a window named 'Face Detection'
        # cv2.imshow() creates a window to show the image
        cv2.imshow('Face Detection', img)

        # Exit the loop when the 'Esc' key is pressed (key code 27)
        if cv2.waitKey(1) == 27:  # Press 'Esc' to exit
            break

    # Release the webcam resource 
    cap.release()
    
    # Close all OpenCV windows
    cv2.destroyAllWindows()

detect_face()