
"""
    초음파 센서를 활용한 서보모터 제어

    초음파 센서 : HC-SR04
    서보모터    : SG-90
      - 노란색 : Data
      - 주황색 : VCC
      - 갈색   : GND
"""

from __future__ import print_function
import time
import RPi.GPIO as GPIO

def measure():
    GPIO.output(GPIO_TRIGGER, True)
    time.sleep(0.00001)
    
    GPIO.output(GPIO_TRIGGER, False)
    start = time.time()

    while ( GPIO.input(GPIO_ECHO) == 0 ) :
        start = time.time()

    while ( GPIO.input(GPIO_ECHO) == 1 ) :
        stop = time.time()

    elapsed = stop - start
    distance = (elapsed * 34300) / 2

    return distance

def measure_average() :
    distance1 = measure()
    time.sleep(0.1)

    distance2 = measure()
    time.sleep(0.1)

    distance3 = measure()

    distance = distance1 + distance2 + distance3
    distance = distance / 3

    return distance

GPIO.setmode(GPIO.BCM)

# 서보모터 색상


GPIO_TRIGGER    = 24 
GPIO_ECHO       = 23
servo           = 18            # 서보모터 데이터(노란색)
ledPinNum = 7

print("Ultrasonic Measurement")

GPIO.setup(servo, GPIO.OUT)
GPIO.setup(GPIO_TRIGGER, GPIO.OUT)
GPIO.setup(GPIO_ECHO, GPIO.IN)

GPIO.output(GPIO_TRIGGER, False)

p = GPIO.PWM(servo, 50)
p.start(2.5)

try :
    while True :
        distance = measure_average()
        time.sleep(1)

        if distance <= 10 :
            print("angle : 1")
            p.ChangeDutyCycle(2.5)
            GPIO.output(ledPinNum, True)
        else :
            print("angle : 5")
            p.ChangeDutyCycle(7.5)
            GPIO.output(ledPinNum, False)

except KeyboardInterrupt:
    print("Terminated by Keyboard")
    GPIO.cleanup()

finally :
    print("End of Program")
