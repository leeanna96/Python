number=1234
sum=0
while number>0:
    digit=number%10
    sum+=digit
    number//=10
print("자릿수의 합은",sum,"입니다")
