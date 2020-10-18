n=int(input())
k=[]
for i in range(0,n):
    c=int(input())
    k.append(c)
j=max(k)
for i in k:
    if i==j:
        k.remove(i)
    else:
        continue
print(max(k))
    
