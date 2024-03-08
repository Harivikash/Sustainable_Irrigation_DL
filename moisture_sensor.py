# pip install RPi.GPIO

from gpiozero import DigitalInputDevice
import time

def moisture_sensor():
    sensor_pin = 17  # GPIO pin where the sensor is connected
    moisture_sensor = DigitalInputDevice(sensor_pin)
    if moisture_sensor.value:
        print("Soil is dry")
        return moisture_sensor.value
    else:
        print("Soil is wet")
        return moisture_sensor.value
    # time.sleep(1)
