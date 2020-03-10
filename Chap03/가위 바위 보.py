from random import *
i = randint(1, 3)
if i==1:
    com="가위"
elif i==2:
    com="바위"
else:
    com="보"
s=input("(가위,바위,보)중에서 하나를 선택하세요: ")
print("사용자:",s,"컴퓨터:",com)
if s==com:
    print("비겼음")
elif s=="가위":
    if com=="바위":
        print("컴퓨터가 이겼음")
    else:
        print("사용자가 이겼음")
elif s=="바위":
    if com=="가위":
        print("사용자가 이겼음")
    else:
        print("컴퓨터가 이겼음")
elif s=="보":
    if com=="가위":
        print("컴퓨터가 이겼음")
    else:
        print("사용자가 이겼음")
