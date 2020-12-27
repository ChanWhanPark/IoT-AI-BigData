year = 0
month = 0

year = int(input("연도 입력: "))
month = int(input("월 입력: "))

if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
    print("31일")
elif month == 4 or month == 6 or month == 9 or month == 11:
    print("30일")
elif month == 2:
    if (year % 4 == 0) and (year % 100 != 0) or (year % 400 == 0):
        print("29일")
    else:
        print("28일")
