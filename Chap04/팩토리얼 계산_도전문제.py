i=1
fac=1
num=int(input("정수 입력: "))

while i<=num:
    fac*=i
    i+=1

print(num,"!은", fac,"입니다")
