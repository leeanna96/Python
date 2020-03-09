age=int(input("나이를 입력하시오: "))

if age<=12:
    print("어린이")
elif 13<=age<=18:
    print("청소년")
elif 19<=age<=30:
    print("청년")
elif 31<=age<=50:
    print("장년")
else:
    print("노년")
