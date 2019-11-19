import RPi.GPIO as GPIO
import time

class Motor:
    
    def __init__(self, control_pins=[11,12,13,15]):
        
        # PINES QUE POLARIZAN AL MOTOR
        self.control_pins = control_pins
        
        # CONFIGURAMOS LOS PINES DEL MOTOR
        GPIO.setmode(GPIO.BOARD)
        for pin in self.control_pins:
          GPIO.setup(pin, GPIO.OUT)
          GPIO.output(pin, 0)
        
        # SECUENCIA DE GIRO DEL MOTOR
        self.sequence = [
          [1,0,0,0],
          [1,1,0,0],
          [0,1,0,0],
          [0,1,1,0],
          [0,0,1,0],
          [0,0,1,1],
          [0,0,0,1],
          [1,0,0,1]
        ]
    
    def rotateForward(self, spins):
        for i in range(512*spins):
          for halfstep in range(8):
            for pin in range(4):
              GPIO.output(self.control_pins[pin], self.sequence[halfstep][pin])
            time.sleep(0.001)
        #GPIO.cleanup()
        
    def rotateBackward(self, spins):
        for i in range(512*spins):
          for halfstep in range(8):
            for pin in range(4):
              GPIO.output(self.control_pins[pin], self.sequence[::-1][halfstep][pin])
            time.sleep(0.001)
        #GPIO.cleanup()
