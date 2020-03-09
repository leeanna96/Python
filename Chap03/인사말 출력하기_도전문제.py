import time
now = time.localtime()

if now.tm_month<2 :
    print("겨울")
elif now.tm_month<5:
    print("봄")
elif now.tm_month<9:
    print("여름")
elif now.tm_month<11:
    print("가을")
else:
    print("겨울")
