answer=5
print("숫자 게임에 오신 것을 환영합니다")
while True:
    n=int(input("숫자를 맞춰보세요: "))
    if n==answer:
        print("사용자가 이겼습니다.")
        break
    elif n>answer:
        print("너무 큼")
    else:
        print("너무 작음")
print("게임 종료")
