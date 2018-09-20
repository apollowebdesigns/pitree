from nanpy import ArduinoApi
from nanpy import SerialManager
from time import sleep
import pprint
pp = pprint.PrettyPrinter(width=41, compact=True)

connection = SerialManager(device='/dev/ttyUSB0')

trigPin = 9
echoPin = 10

a = ArduinoApi(connection=connection)
a.pinMode(trigPin, a.OUTPUT)
a.pinMode(echoPin, a.INPUT)

print('what is in the arduino api?')
pp.pprint(a)


def loop():
  a.digitalWrite(trigPin, a.LOW)
  sleep(2/10000)
  # Sets the trigPin on HIGH state for 10 micro seconds
  a.digitalWrite(trigPin, a.HIGH)
  sleep(1/10000)
  a.digitalWrite(trigPin, a.LOW)
  # Reads the echoPin, returns the sound wave travel time in microseconds
  duration = a.pulseIn(echoPin, a.HIGH)
  print('what is the duration?')
  print(duration)
  # Calculating the distance
  distance = duration*0.034/2
  print('what is the distance?')
  print(distance)
  # Prints the distance on the Serial Monitor
  print("Distance: ")
  print(distance)

while True:
    loop()

# for i in range(0, 8):
#     a.digitalWrite(13, a.HIGH)
#     sleep(2)
#     a.digitalWrite(13, a.LOW)
#     sleep(2)