from flask import Flask, render_template,request
import time
import requests
import cv2
import numpy as np
from ultralytics import YOLO
from PIL import Image
import matplotlib.pyplot as plt
import json

app = Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

# noOfFlowers=0


@app.route('/')
def home():
    # if request.method =='POST':
    #     pass
    return render_template('index.html')

@app.route('/weather', methods=['GET','POST'])
def weather():
    if request.method =='POST':
        latitude = request.form.get('latitude')
        longitude = request.form.get('longitude')
        if request.method == 'POST':
            latitude = request.form.get('latitude')
            longitude = request.form.get('longitude')
            
            # Fetch weather data
            weather_data = get_weather_data(latitude, longitude)

            # Save weather data to a JSON file
            with open('weather_data.json', 'w') as file:
                json.dump(weather_data, file)
        weather_data= get_weather_data(latitude, longitude)
        return render_template('index.html',weather_data=weather_data)
    return render_template('index.html')

def get_weather_data(latitude, longitude):
    api_key = '540300516678450432c4b06efd0b07df'
    weather_api_url = f'https://api.openweathermap.org/data/2.5/weather?lat={latitude}&lon={longitude}&appid={api_key}&units=metric'
    response = requests.get(weather_api_url)
    print(latitude,longitude)
    weather_data = response.json()
    return weather_data

# def moisture_data():
@app.route('/webcam')
def webcam():
    # Open webcam and capture an image
    cap = cv2.VideoCapture(0)
    ret, frame = cap.read()
    cap.release()

    # Perform YOLO prediction 
    predicted_result = yolo_prediction(frame)
    timestamp = int(time.time())
    noOfFlowers = predicted_result
    growthStage=growth_stage(noOfFlowers)
    if growth_stage=='flowering stage':
        water_needed=10     #water needed for flowering stages
    else:
        water_needed=5      #water needed during early stages
    return render_template('webcam.html', predicted_result=predicted_result, timestamp=timestamp,growthStage=growthStage)


def yolo_prediction(image):
    # Implement YOLO prediction logic (replace with your YOLO model code)
    # This is a placeholder, you should integrate your YOLO model here
    model = YOLO(r"C:\Users\mhari\Desktop\Flower-detector-1\runs\detect\model32\weights\best.pt")
    pil_image = Image.fromarray(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
    results = model(pil_image,conf=0.8) # results list]
    # pil_image.save("static/webcam.jpg")
    # predicted_result = __len__(results)
    for r in results:
        im_array = r.plot()  # plot a BGR numpy array of predictions
        im = Image.fromarray(im_array[..., ::-1])  # RGB PIL image
        im.save("static/webcam.jpg")
        # im.show()
        
    

    # Save YOLO predictions to a file
    if len(results[0])>0:
        predictions = {"object_detected": 1, "class": "flower"}
    else:
        predictions = {"object_detected": 0, "class": "flower"}
        
    # print(len(results[0].boxes.conf.numpy()))
    with open('yolo_predictions.json', 'w') as file:
        json.dump(predictions, file)

    return len(results[0])

def growth_stage(noOfFlowers):
    if noOfFlowers>=1:
        return 'flowering stage'
    else:
        return 'not yet reached flowering stage'
    
    

if __name__ == '__main__':
    app.run(debug=True)
