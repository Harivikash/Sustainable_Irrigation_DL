%pip install RPi.GPIO

from gpiozero import DigitalInputDevice
import time

sensor_pin = 17  # GPIO pin where the sensor is connected
moisture_sensor = DigitalInputDevice(sensor_pin)

while True:
    if moisture_sensor.value:
        print("Soil is dry")
    else:
        print("Soil is wet")
    time.sleep(1)
