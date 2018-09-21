from nanpy import ArduinoApi
from nanpy import SerialManager
from time import sleep

connection = SerialManager(device='/dev/ttyACM0')

trigPin = 9
echoPin = 10

a = ArduinoApi(connection=connection)
# a.pinMode(trigPin, a.OUTPUT)
# a.pinMode(echoPin, a.INPUT)

from nanpy import Ultrasonic

ultrasonic = Ultrasonic(echoPin, trigPin, False, connection=connection)

def test():
    print(ultrasonic.get_distance())
    sleep(0.000002)

while True:
    test()