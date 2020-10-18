n=int(input())
lst=[]
for i in range(0,n):
    c=input()
    lst.append(c)
s=set()
p=[]
for i in range(0,len(lst)):
    k=1
    if lst[i] not in s:
        for j in range(i+1,len(lst)):
            if lst[i]==lst[j]:
                k=k+1
                s.add(lst[i])
        p.append(k)
print(len(p))
for i in p:
    print(i,end=' ')
        
    
    
    
        
    
