time=int(input("근무시간을 입력하시오: "))
wage=int(input("시간당 임금을 입력하시오: "))

if time>=40:
    TotalWages=(time-40)*1.5*wage + 40*wage
else:
    TotalWages=time*wage
print("총임금은", TotalWages)
