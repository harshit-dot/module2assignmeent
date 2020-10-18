n,m=input().split()
n=int(n)
m=int(m)
lst=[]
lst1=[]
for i in range(0,n):
    c=input()
    lst.append(c)
for i in range(0,m):
    d=input()
    lst1.append(d)

for i in range(0,m):
    s=0
    for j in range(0,n):
        if lst1[i]==lst[j]:
            print(j+1,end=' ')
            s=s+1
    if s==0:
        print('-1')
    else:
        
        print()
    
            
            

    
