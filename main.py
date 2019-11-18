import requests
import time
from gpiozero import DistanceSensor
from time import sleep
from Proximity import Proximity
from Control import Control
from Motor import StepperMotor

from config import *

sensor = DistanceSensor(23,24)
proximity = Proximity(sensor)
actuators = {'motor': StepperMotor(), 'water': None}

control = Control(actuators)

# Aquí debemos hacer un diccionario con el motor

# Obtenemos la información de todos los sensores
def getSystemInfo():
    distance = proximity.getDistance()
    light = light.getLight()
    humidity = humidity.getHumidity()

    info = {'distance': distance, 'light': light, 'humidity': humidity}
    return info




while True:
    #OBTENEMOS LA DISTANCIA ACTUAL
    info  = getSystemInfo()    
    
    # ENVIAMOS LOS DATOS
    response = requests.post( url = URL, params = info )

    # Actualizamos el controlador del sistema con los datos
    control.update(info)
    control.activate()

    # OBTENEMOS LA RESPUESTA
    print(response.json())
    
    # ESPERAMOS UN SEGUNDO PARA LA SIGUIENTE PETICION
    time.sleep(REFRESH_RATE)
