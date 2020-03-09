import math

A=float(input("A = "))
B=float(input("B = "))
C=float(input("C = "))
x=-10000

while True:
    y=A*x*x+B*x+C
    if -10000<=x<=10000:
        if y==0:
            xx=x
            break
        else:
            x+=1
    else:
        break

print("근은", xx)
