# main_module.py
import json
import numpy as np
from weather import get_weather_data
from yolo_prediction import yolo_prediction
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
from tensorflow.keras.models import model_from_json
from camera_webcam import capture_image  # for windows webcam
# from camera_module import capture_image # for raspberry pi camera module
# from moisture_sensor import moisture_sensor # use after moisture sensor is connected to raspberry pi

# Load the model architecture from the saved JSON file
with open("lstm_model.json", "r") as json_file:
    loaded_model_json = json_file.read()

# Create the model based on the loaded architecture
loaded_model = model_from_json(loaded_model_json)

# Load the trained weights into the model
loaded_model.load_weights("lstm_model_weights.h5")

# Load weather data
weather_data=get_weather_data()

#Load yolo_prediction
image=capture_image()
yolo_predictions=yolo_prediction(image)

# with open('weather_data.json', 'r') as file:
#     weather_data = json.load(file)

# # Load YOLO predictions
# with open('yolo_predictions.json', 'r') as file:
#     yolo_predictions = json.load(file)

# Extract relevant data
gust_data = weather_data["wind"]["speed"]
precipitation_data = 0  # Replace with actual data
pressure_data = weather_data["main"]["pressure"]
temperature_data = weather_data["main"]["temp"]
moisture_data = 500  # Replace with actual data
growth_stage_data = yolo_predictions["object_detected"]

# check the parameters
print(gust_data,precipitation_data,pressure_data, temperature_data, moisture_data, growth_stage_data)

# combine into unified data
to_be_predicted = np.column_stack((gust_data, precipitation_data, pressure_data, temperature_data, moisture_data, growth_stage_data))

# Normalize the new data
scalar=MinMaxScaler()
to_be_predicted = scalar.fit_transform(to_be_predicted)

# Reshape data for LSTM input
to_be_predicted = to_be_predicted.reshape((to_be_predicted.shape[0], to_be_predicted.shape[1], 1))

# Make predictions using the loaded model
predictions = loaded_model.predict(to_be_predicted)

print(predictions[0][0])
