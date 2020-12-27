
"""
3개의 변수를 입력받고,
최대값, 최소값, 합계, 평균을 구하라"
"""

# 변수 선언
aVal = 0        # 정수 1 입력
bVal = 0        # 정수 2 입력
dVal = 0        # 정수 3 입력
maxVal = 0      # 최대값
minVal = 0      # 최소값
tmpVal = 0      # 임시저장값
sumVal = 0
avgVal = 0.0

aVal = int(input("정수1 입력 : "))
bVal = int(input("정수2 입력 : "))
dVal = int(input("정수3 입력 : "))

maxVal = aVal
if ( maxVal > bVal ) :
    if ( maxVal < dVal ) :
        maxVal = dVal

elif ( maxVal < bVal ) :
    maxVal = bVal
    if ( maxVal < dVal ) :
        maxVal = dVal

maxVal = max(aVal, bVal, dVal)
minVal = min(aVal, bVal, dVal)







    
