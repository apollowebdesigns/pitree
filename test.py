from time import sleep
from nanpy import ArduinoApi
from nanpy import SerialManager
connection = SerialManager(device='/dev/ttyUSB0')

a = ArduinoApi(connection=connection)
a.pinMode(13, a.OUTPUT)
a.digitalWrite(13, a.HIGH)
sleep(3)
a.digitalWrite(13, a.LOW)

