from nanpy import ArduinoApi
from nanpy import SerialManager
from time import sleep

connection = SerialManager(device='/dev/ttyUSB0')

trigPin = 9
echoPin = 10

a = ArduinoApi(connection=connection)
a.pinMode(trigPin, a.OUTPUT)
a.pinMode(trigPin, a.INPUT)


def loop():
  a.digitalWrite(trigPin, a.LOW)
  sleep(0.2)
  # Sets the trigPin on HIGH state for 10 micro seconds
  a.digitalWrite(trigPin, a.HIGH)
  sleep(0.1)
  a.digitalWrite(trigPin, a.LOW)
  # Reads the echoPin, returns the sound wave travel time in microseconds
  duration = a.PulseIn(echoPin, a.HIGH)
  # Calculating the distance
  distance = duration*0.034/2
  # Prints the distance on the Serial Monitor
  print("Distance: ")
  print(distance)


# for i in range(0, 8):
#     a.digitalWrite(13, a.HIGH)
#     sleep(2)
#     a.digitalWrite(13, a.LOW)
#     sleep(2)