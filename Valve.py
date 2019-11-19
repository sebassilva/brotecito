from gpiozero import Motor
from time import sleep
import threading


def openValve(self, motor):
        print("Abriendo Valvula")
        motor.forward()
        sleep(5)
        print("Cerrando Valvula")

        

class Valve():
    def __init__(self):
        self.motor = Motor(forward=4, backward=14)
    
    def open(self):
        print("Abriendo Valvula")
        x = threading.Thread(target=openValve, args=(self.motor,))
        x.start()


def test():
    valve = Valve()
    valve.open()

test()