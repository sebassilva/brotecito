import requests
import time
from random import random
from gpiozero import DistanceSensor
from time import sleep
from config import *

sensor = DistanceSensor(tiggerPin,echoPin)

#while True:
#    print('Distance to nearest is', sensor.distance, 'm')
#    sleep(1)

while True:
    #print('Distance to nearest is', sensor.distance*100, 'cm')
    distance = int(sensor.distance*100)
    PARAMS = {'distance':distance}
    response = requests.post( url = URL, params = PARAMS )
    try:
        print(response.json())
    except:
        print('error', response)
    time.sleep(1)