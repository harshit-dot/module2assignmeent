t=int(input())
for i in range(0,t):
    n,x,p,k=map(int,input().split())
    lst=list(map(int,input().split()))
    o=1
    j=0
    f=0
    if len(lst)>k:
        while True:
            if lst[p-1]==x:
                print(f)
                break
            if x not in lst:
                lst[k]=x
                s=lst
                s.sort()
                if s[p-1]==x:
                    print(o)
                else:
                    print('-1')
                break
            if x in lst:
                for i in range(0,k):
                    lst[k]=j
                    f=f+1
                    g=lst
                    g.sort()
                    if g[p-1]==x:
                        h=1
                        print(f)
                        break
                    else:
                        j=j+1
                if h!=1:
                    print('-1')
                    break
   
       
    else:
        if lst[p-1]==x:
            print(f)
        else:
            print('-1')
        
            
                    
    
  
   
    

    
        
    
        
        
    
