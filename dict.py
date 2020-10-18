k=[]
g=[]
n=int(input())
for i in range(0,n):
    a,b=input().split()
    b=int(b)
    k.append(a)
    g.append(b)
f=[]
s=set()
for i in range(0,len(k)):
    if k[i] not in s:
        for j in range(i+1,len(k)):
            if k[i]==k[j]:
                g[i]=g[i]+g[j]
        s.add(k[i])
        h=[k[i],g[i]]
        f.append(h)
for i in f:
    print(i[0], i[1])    
    
            
               
