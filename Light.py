from gpiozero import LightSensor, PWMLED
from signal import pause
from time import sleep
import RPi.GPIO as GPIO

# Clase que define el comportamiento de el sensor de luz
class Light():
    def __init__(self, sensor_pin=18):
        #GPIO.setmode(GPIO.BOARD)
        self.sensor = LightSensor(sensor_pin)

    def getValue(self):
        return self.sensor.value


def test():
    light = Light()
    while True:
        print("Luz actual: " + str(light.getValue()))
        sleep(0.5)


# test()