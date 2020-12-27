import RPI.GPIO as g
import Adafruit_DHT as dht
import datetime
import time

DHT_Sensor = Adafruit_DHT.DHT11 #DHT22
pinNum = 24

def readData():
    hum, temp = Adafruit_DHT.read_retry(DHT_Sensor, pinNum)
    wtime = datetime.now()

    if hum is not None and temp is not None:
        print("습도 : " + str(hum))
        print("온도 : " + str(temp))
        print("시간 : " + str(wtime))
    else:
        print("값 없음")

def main():
    try:
        readData()
    except KeyboardInterrupt e:
        print(e)
        print("키보드 입력으로 종료")
    finally:
        g.cleanup()
        print("프로그램 종료")
    
        
            
        
if __name__ == "__main__":
    main()
