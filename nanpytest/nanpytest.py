from nanpy import ArduinoApi
from nanpy import SerialManager
from time import sleep

connection = SerialManager(device='/dev/ttyACM0')

trigPin = 9
echoPin = 10

a = ArduinoApi(connection=connection)

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