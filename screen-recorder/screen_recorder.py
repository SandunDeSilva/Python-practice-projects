# Import the OpenCV library for computer vision tasks
import cv2
# Import NumPy for handling arrays and numerical operations
import numpy as np
# Import ImageGrab from PIL to capture the screen
from PIL import ImageGrab

def screen_recorder():
    # Define the codec and create a VideoWriter object to save the video
    # 'XVID' is a popular video codec; 5.0 is the frame rate
    # (1366, 768) is the resolution of the captured video
    fourcc = cv2.VideoWriter_fourcc(*"XVID")
    out = cv2.VideoWriter("output.avi", fourcc, 20.0, (1366, 768))

    # Infinite loop to continuously capture the screen
    while True:
        # Capture the screen using PIL's ImageGrab.grab()
        img = ImageGrab.grab()

        # Convert the PIL image to a NumPy array for OpenCV compatibility
        img_np = np.array(img)

        # Convert the color format from BGR (OpenCV default) to RGB (PIL default)
        # OpenCV uses BGR by default, while PIL uses RGB
        frame = cv2.cvtColor(img_np, cv2.COLOR_RGB2BGR)

        # Display the captured frame in a window named "Screen Recorder"
        # This allows you to see what is being recorded in real-time
        # cv2.imshow() creates a window to show the image
        # cv2.waitKey(1) waits for 1 millisecond for a key event
        cv2.imshow("Screen Recorder", cv2.WINDOW_NORMAL)

        # Write the frame to the video file
        # This saves the captured frame to the output video file
        out.write(frame)

        # Check if the 'Esc' key (key code 27) is pressed to exit the loop
        # If the 'Esc' key is pressed, break the loop and stop recording    
        if cv2.waitKey(10) == 27:
            break

    # Release the VideoWriter object and close all OpenCV windows
    # This ensures that the video file is properly saved and resources are released
    out.release()

    # Close all OpenCV windows
    cv2.destroyAllWindows()

screen_recorder()
    