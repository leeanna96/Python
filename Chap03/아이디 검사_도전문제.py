id_list=['김철수', '홍길동', '김영희']
pw_list=['12345678', '1234']

id=input("아이디를 입력하시오: ")
if id in id_list:
    pw=input("패스워드를 입력하시오: ")
    if pw in pw_list:
        print("환영합니다!")
    else:
        print("잘못된 패스워드입니다")
else:
    print("알 수 없는 사용자입니다!")


