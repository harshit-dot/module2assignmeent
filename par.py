from itertools import combinations_with_replacement

n,m=input().split()
m=int(m)
    
k=list((combinations_with_replacement(n,m)))
for i in range(0,len(k)):
    k[i]=sorted(k[i])
k.sort()
for i in k:
    for j in i:
        print(j,end='')
    print()
    k=[]
            
        
        
