class Proximity:
    
    def __init__(self, sensor):
        self.sensor = sensor
        
    def getDistance(self):
        return int(self.sensor.distance*100)