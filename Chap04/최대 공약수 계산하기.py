x=int(input("큰 수 입력:"))
y=int(input("작은 수 입력:"))

while y!=0:
    r=x%y
    x,y=y,r
print("최대 공약수는 %d입니다" %x)
