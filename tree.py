import pprint
from time import sleep
from gpiozero import LEDBoard
from gpiozero.tools import random_values
from signal import pause
tree = LEDBoard(*range(2,28),pwm=True)
print('what is the tree?')
#pprint(tree)
#tree = LEDBoard(2,pwm=True)
def light_tree():
  tree.on()

def dim_tree():
  tree.off()
#for led in tree:
# led.source_delay = 0.1
# #led.source = [1, 1, 1, 1, 1, 1,1, 1, 1,1, 1, 1,1, 1, 1,1, 1, 1,1, 1, 1,1, 1,$
# led.source = [1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0] 
# print(led.source)
#pause()

