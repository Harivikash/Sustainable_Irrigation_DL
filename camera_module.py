from picamera import PiCamera
from time import sleep

def capture_image(file_path="image.jpg"):
    try:
        # Initialize the PiCamera
        camera = PiCamera()

        # Optional: Adjust camera settings if needed (e.g., resolution, rotation, etc.)
        # camera.resolution = (1920, 1080)
        # camera.rotation = 180

        # Warm up the camera
        sleep(2)

        # Capture an image
        camera.capture(file_path)
        print(f"Image captured successfully: {file_path}")

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    capture_image()
