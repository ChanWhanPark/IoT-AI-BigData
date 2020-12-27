num1 = 0
num2 = 0

num1 = int(input("정수 1 입력: "))
num2 = int(input("정수 2 입력: "))

if num1 >= num2:
    print("큰 수 : %d, 작은 수 : %d" % (num1, num2))
    print("차 : %d" % (num1 - num2))
else:
    print("큰 수 : %d, 작은 수 : %d" % (num2, num1))
    print("차 : %d" % (num2 - num1))
