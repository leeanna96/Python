str=input("문자열을 입력하시오: ")
length = len(str)
if length%2==0:
    index=length//2
    print("중앙글자는", str[index-1], str[index])
else:
    index=length//2
    print("중앙글자는", str[index])
