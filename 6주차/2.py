n1 = int(input("시작값 : "))
n2 = int(input("종료값 : "))

if (n1 > n2):
    n3 = -1
else:
    n3 = 1

sumVal = 0
for i in range(n1, n2, n3):
    sumVal += i
    print(sumVal)


print("========================")
print(str(sumVal))
