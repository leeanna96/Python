shape=int(input("도형을 입력하시오(1: 사각형, 2: 삼각형, 3: 원): "))
if shape==1:
    x=int(input("가로: "))
    y=int(input("세로: "))
    area=x*y
elif shape==2:
    x=int(input("밑변: "))
    h=int(input("높이: "))
    area=x*h/2
else:
    r=int(input("반지름: "))
    area=r*r*3.14
print(area)
