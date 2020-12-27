"""
신용카드의 잔고(청구액)을 계산하고
사용한도액을 초과했는지를 결정

카드 번호, 잔고, 총 사용액, 총 환불액,
신용한도액 입력 받음 
새 잔고 계산식 
(월초 잔고 + 총 사용액 - 총 환불액)
"""

aVal = 0        # 카드번호
bVal = 0        # 잔고번호
dVal = 0        # 총 사용액 
eVal = 0        # 총 환불액
fVal = 0        # 신용카드 한도
totalVal = 0

aVal = int(input("카드번호 입력"))
dVal = int(input("총 사용액 입력"))
eVal = int(input("총 환불액 입력"))
fVal = int(input("신용카드 한도 입력"))
bVal = int(input("잔고 입력"))

totalVal = bVal + dVal - eVal


if (fVal < totalVal ) :
    print("사용할 수 있는 잔액이 없습니다.")
else :
    print("사용할 수 있는 잔액 : ",
          fVal - totalVal )



