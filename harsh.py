from itertools import product
a=input()
k=a.split()
for i in range(0,len(k)):
    k[i]=int(k[i])
b=input()
g=b.split()
for i in range(0,len(g)):
    g[i]=int(g[i])
m=list(product(k,g))
for i in range(0,len(m)):
    print(m[i],end=' ')


