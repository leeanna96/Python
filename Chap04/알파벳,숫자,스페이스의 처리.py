str=input("문자열을 입력하시오:")

alpha=0
digit=0
space=0

for c in str:
    if c.isalpha():
        alpha+=1
    if c.isdigit():
        digit+=1
    if c.isspace():
        space+=1
print("알파벳의 수:", alpha)
print("숫자의 수:", digit)
print("스페이스의 수:",space)

