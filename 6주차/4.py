first_num = 0
last_num = 0
pm = 0


sumVal = 0
first_num = int(input("시작값 입력: "))
last_num = int(input("종료값 입력: "))
pm = int(input("증감값 입력: "))

if ((first_num < last_num and pm < 0) or (first_num > last_num and pm > 0)):
    print("잘못된 증감식으로 합은 0으로 출력됩니다.")


for i in range(first_num, last_num, pm):
    sumVal += i
    print(sumVal)

print("===========================")
print(str(first_num) + "과 " + str(last_num) + "까지 " + str(pm) +
      "씩 증가하여 더한 값은 " + str(sumVal))
