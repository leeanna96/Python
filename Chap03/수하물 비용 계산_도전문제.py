count=int(input("짐의 개수는 몇개입니까?"))
price=0
if count>=2:
    price+=30000
while count>0:
    weight=int(input("짐의 무게는 얼마입니까?"))
    if weight>=20:
        price+=20000
    count-=1
print("짐에 대한 수수료는", price,"원 입니다")
print("감사합니다.")
