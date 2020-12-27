import random

aval = 0
bval = 0
aval = random.randrange(1, 7)
bval = random.randrange(1, 7)

print("A : %d  B: %d" % (aval, bval))
if aval > bval:
    print("A가 이겼습니다.")
elif aval < bval:
    print("B가 이겼습니다.")
else:
    print("비겼습니다.")
