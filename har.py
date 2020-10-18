t=int(input())
for i in range(0,t):
    n,d=map(int,input().split())
    k=list(map(int,input().split()))
    sm=sum(k)
    s=0
    l=0
    for i in range(0,n-1):
        if k[i]<d:
            s=1
            l=i
            break
        k[i+1]=k[i+1]+(k[i]-d)
    if s==1:
        print(l+1)
    else:
        l=(sm//d)+1
        print(l)
            
            
        
