n=int(input())
m=input().split()[:n]
k=set()
k.update(m)
p=len(k)
s=0
for i in k:
    s=s+int(i)
g=s/p
print('{:.2f}'.format(g))
    
