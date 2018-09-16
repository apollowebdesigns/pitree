import serial #Import Serial Library
from tree import light_tree, dim_tree

# current address of arduino on which serial port
arduinoSerialData = serial.Serial('/dev/ttyUSB0',9600) #Create Serial port object called arduinoSerialData

def get_dist():
    while (1==1):
        if (arduinoSerialData.inWaiting()>0):
            myData = arduinoSerialData.readline()
            print(myData.decode())
            if(float(myData.decode()) < 5):
                light_tree()
            else:
                dim_tree()
