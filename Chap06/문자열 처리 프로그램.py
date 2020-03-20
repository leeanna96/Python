dog=[]
while True:
    name=input("강아지의 이름을 입력하시오(종료시에는 엔터키): ")
    if name=="":
        break

    dog.append(name)

print("강아지들의 이름:")
for name in dog:
    print(name, end=", ")
