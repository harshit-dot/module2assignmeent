n=int(input())


s=list()
for i in range(0,n):
    c=input().split()
    if c[0]=='print':
        print(s)
    elif c[0]=='append':
        b=int(c[1])
        
        s.append(b)
    elif c[0]=='insert':
        b=int(c[1])
        d=int(c[2])
        s.insert(b,d)
    elif c[0]=='remove':
        b=int(c[1])
        s.remove(b)
    elif c[0]=='pop':
        s.pop()
    elif c[0]=='sort':
        s.sort()
    elif c[0]=='reverse':
        s.reverse()

    
        

    
