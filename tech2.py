n=int(input())
m=int(input())
lst=[]
for i in range(0,n):
    for j in range(0,1):
        c=input().split()[:m]
        lst=lst+c
print(lst) 
s=0
c=[]
for i in lst:
    s=s+int(i)
    c.append(s)
print(c)
k=0
for i in range(0,n):
    for j in range(k,k+m):
        print(c[j],end=' ')
    k=k+m
        
    print()
    
    
    
    
    
