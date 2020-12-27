odd = 0
even = 0


for i in range(0, 10):
    numVal = int(input("정수 %d 입력 : " % (i+1)))
    if (numVal % 2 == 0):
        even = even + 1
    else:
        odd = odd + 1


print("홀수 개수 : %d\t짝수 개수: %d" % (odd, even))
