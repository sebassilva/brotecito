class Control():
    


    def __init__(self, actuators):
        self.distance = 0.0
        self.light = 0.0
        self.humidity = 0.0
        self.time_of_light = 0.0
        self.is_covered = False
        self.motor = actuators.get('motor')  # instance of motor
        self.water = actuators.get('water')  # instance of water
        self.MIN_HUMIDITY = 0.3
        self.MIN_LIGHT = 0.3
        self.MAX_LIGHT = 0.7



    def update(self, data): 
        self.distance = data.get('distance')
        self.light = data.get('light')
        self.humidity = data.get('humidity')
        # Si esta cubierta y recibe luz, es de dia. Incrementamos time_of_light
        if not self.is_covered and self.light >= self.MIN_LIGHT:
            self.time_of_light += 1


    # Regresa True si esta seca la planta
    # False de cualquier otra forma
    def should_water_plant(self):
        if self.humidity <= self.MIN_HUMIDITY:
            return True
        return False
    
    # Controla el motor si ya recibio suficiente luz

    def should_cover_plant(self):
        if self.light >= self.MAX_LIGHT:
            return True
        return False

    def activate(self):
        print('Iniciando protocolo de activacion')
        if self.should_cover_plant():
            print("Cubriendo planta del sol")
            self.motor.rotateForward(1)
        
        if self.should_water_plant():
            print("Regando la planta")
            #self.water.water()  ## cambiar por lo que sea que haga que caiga el agaua



    