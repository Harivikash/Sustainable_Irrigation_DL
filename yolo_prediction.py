# yolo_prediction.py
import cv2
from ultralytics import YOLO
from PIL import Image
import json

def yolo_prediction(image):
    model = YOLO(r"C:\Users\mhari\Desktop\Flower-detector-1\runs\detect\model32\weights\best.pt")
    pil_image = Image.fromarray(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
    results = model(pil_image, conf=0.8)

    # Save YOLO predictions to a file
    if len(results[0]) > 0:
        predictions = {"object_detected": 1, "class": "flower"}
        return predictions
    else:
        predictions = {"object_detected": 0, "class": "flower"}
        return predictions

    # with open('yolo_predictions.json', 'w') as file:
    #     json.dump(predictions, file)

    # return len(results[0])
