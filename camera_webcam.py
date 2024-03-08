import cv2

def capture_image(file_path="image.jpg"):
    try:
        # Initialize the webcam (adjust the index based on your webcam)
        cap = cv2.VideoCapture(0)

        # Check if the webcam is opened successfully
        if not cap.isOpened():
            raise Exception("Error: Unable to open webcam.")

        # Read a single frame from the webcam
        ret, frame = cap.read()

        # Check if the frame is read successfully
        if not ret:
            raise Exception("Error: Unable to capture frame from the webcam.")

        # Save the frame as an image file
        cv2.imwrite(file_path, frame)
        print(f"Image captured successfully: {file_path}")

        # Release the webcam
        cap.release()
        return frame

    except Exception as e:
        print(f"Error: {e}")

