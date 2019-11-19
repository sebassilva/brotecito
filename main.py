import requests
import time
from gpiozero import DistanceSensor
from time import sleep
from Proximity import Proximity
from Control import Control
from Motor import Motor
from Light import Light

from config import *

light = Light()
# try:
#     sensor = DistanceSensor(23,24)
#     proximity = Proximity(sensor)
# except:
#     print("no se pudo obtener el sensor de distancia")

actuators = {'motor': Motor(), 'water': None}
control = Control(actuators)


# Obtenemos la informacion de todos los sensores
def getSystemInfo():
    # try:
    #     distance = proximity.getDistance()
    # except:
    #     print("Error en el sensor de distancia")
    #     distance = 0
    try:
        light = light.getValue()
        print(light)
    except Exception as e:
        print(e)
        print("Error en el sensor de luz")
        light = 0
    try:
        humidity = humidity.getValue()
    except: 
        humidity = False

    distance = 0
    info = {'distance': distance, 'light': light, 'humidity': humidity, 'is_wet': humidity}
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
