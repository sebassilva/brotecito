import RPi.GPIO as GPIO
import time

# Clase que define el comportamiento del sensor de humedad
class Humidity():
    def __init__(self, channel = 21):
        print("Instanciandio eventos")
        #GPIO.cleanup()
        #GPIO.setmode(GPIO.BOARD)
        GPIO.setup(channel, GPIO.IN)
        self.is_humid = False
        GPIO.add_event_detect(channel, GPIO.BOTH, bouncetime=300)  # let us know when the pin goes HIGH or LOW
        GPIO.add_event_callback(channel, self.callback)  # assign function to GPIO PIN, Run function on

 
    def callback(self, channel):
        print("CALLBACK")
        self.is_humid = not self.is_humid

    def getValue(self):
        print("Humidity: " + str(self.is_humid))
        return self.is_humid
 
def test():
    humidity = Humidity()
    while True:
        print("humedad actual: " + str(humidity.getValue()))
        time.sleep(1)
#test()