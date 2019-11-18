import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)

control_pins = [11,12,13,15]
LAPS = 1

for pin in control_pins:
  GPIO.setup(pin, GPIO.OUT)
  GPIO.output(pin, 0)
SEQUENCE = [
  [1,0,0,0],
  [1,1,0,0],
  [0,1,0,0],
  [0,1,1,0],
  [0,0,1,0],
  [0,0,1,1],
  [0,0,0,1],
  [1,0,0,1]
]
for i in range(512*LAPS):
  for halfstep in range(8):
    for pin in range(4):
      GPIO.output(control_pins[pin], SEQUENCE[halfstep][pin])
    time.sleep(0.001)
GPIO.cleanup()


class StepperMotor:
    
    def __init__(self):
        
        self.sequence =SEQUENCE = [
          [1,0,0,0],
          [1,1,0,0],
          [0,1,0,0],
          [0,1,1,0],
          [0,0,1,0],
          [0,0,1,1],
          [0,0,0,1],
          [1,0,0,1]
        ]
    
    def rotateForward(self, laps):
        for i in range(512*LAPS):
          for halfstep in range(8):
            for pin in range(4):
              GPIO.output(control_pins[pin], SEQUENCE[halfstep][pin])
            time.sleep(0.001)
        GPIO.cleanup()

motor = StepperMotor()