from nanpy import ArduinoApi
from nanpy import SerialManager
from time import sleep
import pprint
from time import sleep
from gpiozero import LEDBoard
from gpiozero.tools import random_values
from signal import pause

connection = SerialManager(device='/dev/ttyACM0')

trigPin = 9
echoPin = 10

a = ArduinoApi(connection=connection)

tree = LEDBoard(*range(2,28),pwm=True)
print('what is the tree?')
#pprint(tree)
#tree = LEDBoard(2,pwm=True)
def light_tree():
  tree.on()

def dim_tree():
  tree.off()

from nanpy import Ultrasonic

ultrasonic = Ultrasonic(echoPin, trigPin, False, connection=connection)

def test():
    distance = ultrasonic.get_distance()
    print(distance)
    if distance < 5:
        light_tree()
    else:
        tree.off()
    sleep(0.002)

while True:
    test()