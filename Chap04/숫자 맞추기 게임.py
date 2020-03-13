import random

tries=0
number=random.randint(1,100)

print("1부터 100 사이의 숫자를 맞추시오")

while tries<10:
    guess=int(input("숫자를 입력하시오: "))
    tries+=1
    if guess>number:
        print("높음")
    elif guess<number:
        print("낮음")
    else:
        break

if number==guess:
    print("정답")
if tries>10:
    print("정답은", number)
        
