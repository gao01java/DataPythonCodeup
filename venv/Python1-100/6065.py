a,b,c=input().split()

a=int(a)
b=int(b)
c=int(c)


if a%2==0 |b%2==0:
    print(a,b)
elif b%2==0 | c%2==0:
    print(b,c)
elif a%2==0 |c%2==0:
    print(a,c)
elif a%2==0:
    print(a)
elif b%2==0:
    print(b)
elif c%2==0:
    print(c)
elif a % 2 == 0 | b % 2 == 0 | c%2==0:
        print(a, b,c)
