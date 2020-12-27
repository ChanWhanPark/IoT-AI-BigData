n1 = 0
n2 = 0
n3 = 0
n1 = int(input("정수 1을 입력하세요: "))
n2 = int(input("정수 2를 입력하세요: "))
n3 = int(input("정수 3을 입력하세요: "))

Max = 0
Min = 0
if n1 >= n2:
    if n1 >= n3:
        Max = n1
        if n2 >= n3:
            Min = n3
        else:
            Min = n2
    else:
        Max = n3
        Min = n2
else:
    if n1 <= n3:
        Min = n1
        if n2 <= n3:
            Max = n3
        else:
            Max = n2
    else:
        Min = n3
        Max = n2
print("최댓값 : %d, 최솟값 : %d" % (Max, Min))
Sum = n1 + n2 + n3
print("합계 : %d" % Sum)
Avg = Sum / 3
print("평균 : %.2f" % Avg)
