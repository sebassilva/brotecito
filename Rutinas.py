from datetime import timedelta

class Rutinas:
    
    def __init__(self):
        seconds = timedelta()
        pass
    
   def luz(self,sensor):
       sensor.when_light = self.light
       
    def light(self):
        print("Hay luz")
        seconds = seconds + timedelta(seconds=1)
        
       
       