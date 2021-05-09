a,b,c=map(int,input().split())

if a>b>c:
    print(c)
elif a>c>b:
    print(b)
elif b>a>c:
    print(c)
elif b>c>a:
    print(a)
elif c>b>a:
    print(a)
elif c>a>b:
    print(b)
elif c==a==b:
    print(a)