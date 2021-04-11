

n = int(input())
k = list(map(int,input().split()))
a=k[0]
for i in range(n):
    if (a > k[i]):
        a = k[i]
print(a)