from gpiozero import Motor
from time import sleep
import threading


def openValve(self, motor):
        motor.forward()
        sleep(5)
        

class Valve():
    def __init__(self):
        self.motor = Motor(forward=4, backward=14)
    
    def openValveThread(self):
        print("Abriendo Valvula")
        x = threading.Thread(target=openValve, args=(self.motor,))
        x.start()

        print("Cerrando valvula")
    
    def open(self):
        thread.start_new_thread(self.openValveThread, ())



def test():
    valve = Valve()
    valve.open()

test()