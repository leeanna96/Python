itemPrice=int(input("물건값을 입력하시오: "))
note=int(input("1000원 지폐개수: "))
nCoin500=int(input("500원 동전개수: "))
nCoin100=int(input("100원 동전개수: "))

change=note*1000+nCoin500*500+nCoin100*100-itemPrice

nCoin500=change//500
change%=500

nCoint100=change//100
change%=100

nCoin10=change//10
change%=10

nCoin1=change

print("500원=", nCoin500, "100원=",nCoint100,"10원=", nCoin10, "1원=", nCoin1)
