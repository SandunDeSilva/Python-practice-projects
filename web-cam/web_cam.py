import cv2

# Initialize the webcam (0 is usually the default camera)
image_capture = cv2.VideoCapture(0)

# Flag to control the loop – we only want to capture one image
result = True

# Loop to capture a single frame from the webcam
while(result):
    # Read a frame from the webcam
    ret, frame = image_capture.read()

    # Save the captured frame as an image file
    cv2.imwrite("webcam_image.jpg", frame)

    # Set result to False to exit the loop after one capture
    result = False
    print("Image captured and saved as webcam_image.jpg")

# Release the webcam resource
image_capture.release()