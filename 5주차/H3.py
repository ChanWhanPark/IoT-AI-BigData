one = "개"
two = "고양이"
three = "새"

eng_one = "dog"
eng_two = "cat"
eng_three = "새"

Input = int(input("영어명을 보고 싶은 동물번호를 선택하세요."))

if Input == 1:
    print("선택하신 %d번의 %s의 영어명은 %s입니다." % (Input, one, eng_one));
elif Input == 2:
    print("선택하신 %d번의 %s의 영어명은 %s입니다." % (Input, two, eng_two));
elif Input == 3:
    print("선택하신 %d번의 %s의 영어명은 %s입니다." % (Input, three, eng_three));
else:
    print("I don't know");
