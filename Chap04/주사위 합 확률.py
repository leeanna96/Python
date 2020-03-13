from random import randint

count=input("주사위 실험 반복횟수: ")
rollCount=[0,0,0,0,0,0,0,0,0,0,0,0,0]
for i in range(count):
    die1=randint(1,6)
    die2=randint(1,6)
    rollCount[die1+die2]+=1
for i in range(2,13):
    print(i,rollCount[i])

