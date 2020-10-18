n,m=input().split()
n=int(n)
m=int(m)

k=input().split()[:n]
a=input().split()[:m]
b=input().split()[:m]
for i in range(0,len(k)):
    k[i]=int(k[i])
for i in range(0,len(b)):
    a[i]=int(a[i])
    b[i]=int(b[i])
s1=set()
s2=set()
s1.update(a)
s2.update(b)
sm=0

for i in s1:
    for j in k:
        if i==j:
            sm=sm+1
for i in s2:
    for j in k:
        if i==j:
            sm=sm-1
print(sm)

    

