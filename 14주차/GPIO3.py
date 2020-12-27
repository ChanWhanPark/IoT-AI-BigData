import RPi.GPIO as g
import time

g.setmode(g.BCM)

TRIG = 23
ECHO = 25

g.setup(TRIG, g.OUT)
g.setup(ECHO, g.IN)

try:
    while(True):
        g.output(TRIG, g.LOW)
        time.sleep(1)

        g.output(TRIG, g.HIGH)
        time.sleep(0.001)           # 0.001초동안 초음파 송신(40kHz)
        g.output(TRIG, g.LOW)

        # 신호를 수신하지 못한다면
        while(g.input(ECHO) == 0):
            startTime = time.time()

        # 신호를 수신하였다면
        while(g.input(ECHO) == 1):
            endTime = time.time()

        times = endTime - startTime
        # 초음파 신호 344m/s -> *100(cm) / 2(왕복)
        distance = (times * 34400) / 2

        print("distance : " + str(distance) + "cm")
        time.sleep(1)

except KeyboardInterrupt as e:
    print(e)
    print("키보드 입력으로 종료")
finally:
    g.cleanup()
    print("프로그램 종료")
