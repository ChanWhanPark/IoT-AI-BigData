import RPi.GPIO as g
import time

# 서보모터 : 0 ~ 180
# 2.5 ~ 12.5

sPinN = 6
g.setmode(g.BCM)
g.setup(sPin, g.OUT)

p = g.PWM(sPinN, 50) # Hz
p.start(0)

def main():
    try:
        global rotateN # 전역 변수화
        rotateN = 12.5

        while(True):
            p.ChangeDutyCycle(rotateN)
            time.sleep(1)

            rotateN -= 2.5

            if(rotateN < 2.5):
                rotateN = 12.5

    except KeyboardInterrupt as e:
        print("키보드 입력으로 종료")

    finally:
        g.cleanup()
        print("프로그램 종료")

if __name__ == "__main__":
    main()
