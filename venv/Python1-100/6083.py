


r,g,b=map(int,input().split())

d=0

for i in range(r):
    for k in range(g):
        for j in range(b):
            print(i,k,j)
            d += 1

print(d)