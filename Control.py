class Control():
    
    MIN_HUMIDITY = 0.3
    MIN_LIGHT = 0.3
    MAX_LIGHT = 0.7

    def __init__(self, actuators):
        distance = 0.0
        light = 0.0
        humidity = 0.0
        time_of_light = 0.0
        is_covered = False
        motor = actuators.get('motor')  # instance of motor
        water = actuators.get('water')  # instance of water

    def printInfo(self):
        return ", ".join("%s: %s" % item for item in self.items())


    def update(self, data): 
        self.distance = data.get('distance')
        self.light = data.get('light')
        self.humidity = data.get('humidity')
        # Si esta cubierta y recibe luz, es de dia. Incrementamos time_of_light
        if not self.is_covered and self.light >= self.MIN_LIGHT:
            self.time_of_light += 1
        self.printInfo()


    # Regresa True si esta seca la planta
    # False de cualquier otra forma
    def should_water_plant(self):
        if self.humidity <= MIN_HUMIDITY:
            return True
        self.printInfo()
        return False
    
    # Controla el motor si ya recibio suficiente luz

    def should_cover_plant(self):
        if self.light >= MAX_LIGHT:
            return True
        self.printInfo()
        return False

    def activate(self):
        print('Iniciando protocolo de activacion')
        if self.should_cover_plant():
            print("Cubriendo planta del sol")
            self.motor.rotateForward()
        
        if self.should_water_plant():
            print("Regando la planta")
            self.water.water()  ## cambiar por lo que sea que haga que caiga el agaua



    