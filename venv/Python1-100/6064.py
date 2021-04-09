a,b,c=input().split()


a=int(a)
b=int(b)
c=int(c)

d=a if(a<=b) else b
d=d if(d<=c) else c
print(d)


#print((a if a<b else b) if ((a if a<b else b)<c) else c)

#d=(a if a<b else b) if ((a if a<b else b)<c) else c

#print(d)