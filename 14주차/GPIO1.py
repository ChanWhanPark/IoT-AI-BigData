import RPi.GPIO as gpio
import time

pinNum = 23

gpio.setmode(gpio.BCM)
gpio.setup(pinNum, gpio.OUT)


a = 1
while(a<10):
    gpio.output(pinNum, True)
    time.sleep(1)

    gpio.output(pinNum, False)
    time.sleep(1)

    a+=1


