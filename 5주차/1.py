inputVal = 0
resultVal = 0

inputVal = int(input("정수 입력: "))

resultVal = inputVal % 2

if resultVal == 0:
    print(str(inputVal) + "은(는) 짝수입니다.")

else:
    print(str(inputVal) + "은(는) 홀수입니다.")
