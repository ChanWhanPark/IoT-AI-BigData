
# 변수 선언
aVal = 0    # 중간고사 점수
bVal = 0    # 기말고사 점수
dVal = 0    # 과제 점수
eVal = 0    # 출석 점수
totalVal = 0    # 학점 계산

aVal = int(
        input("중간고사 점수 입력(100점기준) :"))
bVal = int(
        input("기말고사 점수 입력(100점기준) :"))
dVal = int(
        input("과제 점수 입력(100점기준) :"))
eVal = int(
        input("출석 점수 입력(100점기준) :"))

totalVal = aVal * 0.2 + bVal * 0.2
            + dVal * 0.4 + eVal * 0.1

if ( totalVal >= 90 ) :
    print("a")
elif ( totalVal >= 80 ) :
    print("b")
elif ( totalVal >= 70 ) :
    print("c")
elif ( totalVal >= 60 ) :
    print("d")
else :
    print("F")
    











