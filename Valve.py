from gpiozero import Motor
from time import sleep
import thread

class Valve():
    def __init__(self):
        self.motor = Motor(forward=4, backward=14)
    
    def openValveThread():
        print("Abriendo Valvula")
        motor.forward()
        sleep(5)
        print("Cerrando valvula")
    
    def open():
        thread.start_new_thread(self.openValveThread)



def test():
    valve = Valve()
    valve.open()

test()