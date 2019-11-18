from gpiozero import LightSensor, PWMLED
from signal import pause
from time import sleep

class Light():
    def __init__(self, sensor_pin=18):
        self.sensor = LightSensor(sensor_pin)

    def getValue(self):
        return self.sensor.value()


def test():
    light = Light()
    while True:
        print("Luz actual: " + str(light.getValue()))
        sleep(0.5)


test()