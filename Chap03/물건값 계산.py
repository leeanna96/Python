price=int(input("구입 금액을 입력하시오: "))

if price>=100000:
    total_price=price*0.95
print("지불 금액은", total_price,"원 입니다")
