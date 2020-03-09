year=int(input("연도를 입력하시오: "))

if year%400==0:
        print("윤년")
elif year%100==0:
    if year%400==0:
        print("윤년")
elif year%4==0:
    if year%100!=0:
        print("윤년")
else:
    print("윤년 아님")
