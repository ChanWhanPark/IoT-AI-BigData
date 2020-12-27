cardNum = int(input("카드 번호 입력: "))
Money = int(input("지난달 잔고 입력: "))
usedMoney = int(input("사용액 입력: "))
refundMoney = int(input("환불액 입력: "))
limitedMoney = int(input("한도액 입력: "))

newMoney = Money + usedMoney - refundMoney

if newMoney > limitedMoney:
    print("%d : 한도초과" % cardNum)
else:
    print("%d : 한도초과되지 않음" % cardNum)
