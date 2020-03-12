year=0
money=1000
interest=float(input("현재 이자율: "))

while money<2000:
    year+=1
    money*=1+interest*0.01
    
print("기간:", year)
print("총액:", money)
