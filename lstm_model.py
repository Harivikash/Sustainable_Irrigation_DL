# Model training

# Import necessary libraries
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics import mean_squared_error
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, LSTM
import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('lstm_dataset.csv')

# Sample data (replace this with your actual data)
Gust_data = df['Gust'].values  # Replace with your weather API data
Precipitation_data = df['Precipitation'].values  # Replace with your weather API data
Pressure_data = df['Pressure'].values  # Replace with your weather API data
Temperature_data = df['Temperature'].values  # Replace with your weather API data
moisture_data = df['MoistureSensor'].values  # Replace with your soil moisture sensor data
growth_stage_data = df['GrowthStage'].values  # Replace with your YOLO model predictions
water_requirement_labels = df['Water_required'].values  # Replace with actual water requirement data

# Combine data into a unified dataset
X = np.column_stack((Gust_data, Precipitation_data, Pressure_data, Temperature_data, moisture_data, growth_stage_data))
y = water_requirement_labels

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Normalize data
scaler = MinMaxScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# Build LSTM model
model = Sequential()
model.add(LSTM(50, input_shape=(X_train.shape[1], 1)))
model.add(Dense(1))
model.compile(optimizer='adam', loss='mse')

# Reshape data for LSTM input
X_train = X_train.reshape((X_train.shape[0], X_train.shape[1], 1))
X_test = X_test.reshape((X_test.shape[0], X_test.shape[1], 1))

# Train the model
history = model.fit(X_train, y_train, epochs=1000, batch_size=32, validation_data=(X_test, y_test), verbose=2)

# Save the model architecture to a file
model_json = model.to_json()
with open("lstm_model.json", "w") as json_file:
    json_file.write(model_json)

# Save the trained weights to a file
model.save_weights("lstm_model_weights.h5")

# Make predictions on test data
predictions = model.predict(X_test)
