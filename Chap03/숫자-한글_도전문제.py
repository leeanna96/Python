num_list=['일','이','삼','사','오','육','칠','팔','구']
num=int(input("숫자를 입력하시오: "))

num100=int(num/100)
num10=int((num-num100*100)/10)
num1=int((num-num100*100)%10)

if num>999:
    print("999를 초과하였습니다")
elif num100>0:
    print(num_list[num100-1],"백")
    if num10>0:
        print(num_list[num10-1],"십")
        if num1>0:
            print(num_list[num1-1])
    else:
        print(num_list[num1-1])
else:
    if num10>0:
        print(num_list[num10-1],"십")
        if num1>0:
            print(num_list[num1-1])
    else:
        print(num_list[num1-1])
