
# 변수 선언
yVal = 0        # 년도 입력
mVal = 0        # 월 입력

yVal = int(input("년도 입력 :"))
mVal = int(input("월 입력 :"))

if ( mVal < 1 or mVal >= 13 ) :
    print("월을 잘못 입력")
else :
    if( mVal == 4 or mVal == 6 or mVal == 9
        or mVal == 11 ) :
        print("30일")
    elif( mVal == 1 or mVal == 3 or mVal == 5
        or mVal == 7 or mVal == 8
        or mVal == 10 or mVal == 12) :
        print("31일")
    else :
        if ( yVal % 4 == 0 and yVal % 100 != 0 )
             or ( yVal % 400 == 0 ) :
                 print("29일")
        else :
            print("28일")













    
