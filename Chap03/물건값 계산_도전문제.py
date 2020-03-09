price=int(input("구입 금액을 입력하시오: "))

if price>=100000:
    total_price=price*0.95
else:
    total_price=price
    change=100000-price
    print(change,"원 만큼 더 구입하면 5% 할인받을 수 있습니다.")
print("지불 금액은", total_price,"원 입니다")
