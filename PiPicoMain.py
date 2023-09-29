from machine import Pin
from time import sleep

led = Pin(25, Pin.OUT)

useful_number= 0

while True:
    led.toggle()
    sleep(.5)
    useful_number += 1
    print("{} is a useful number \nReally.\nSuper useful...\nJust like this script.".format(useful_number))