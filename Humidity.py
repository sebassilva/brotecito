import RPi.GPIO as GPIO
import time

class Humidity():
    def __init__(self, channel = 21):
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(channel, GPIO.IN)
        self.is_humid = False
        GPIO.add_event_detect(channel, GPIO.BOTH, bouncetime=300)  # let us know when the pin goes HIGH or LOW
        GPIO.add_event_callback(channel, self.callback)  # assign function to GPIO PIN, Run function on change
 
 
    def callback(self, channel):
        self.is_humid = not self.is_humid

    def getValue(self):
        return self.is_humid
 

humidity = Humidity()

while True:
    print("humedad actual: " + str(humidity.getValue()))
    #time.sleep(1)
