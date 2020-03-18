def compare():
    a=int(input())
    b=int(input())
    if a>b:
        a,b=b,a
    return a,b

print(compare())
