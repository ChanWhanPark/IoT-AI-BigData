year = 0

year = int(input("연도 입력: "))

if year % 4 == 0 and year % 4 != 0 or year % 400 == 0:
    print("윤년입니다.")

else:
    print("평년입니다.")
