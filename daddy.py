n=int(input('enter the no.of terms'))
d=[]
for i in range(0,n):
    c=int(input())
    d.append(c)
mx=max(d[0],d[1])
sm=min(d[0],d[1])

for i in range(1,n):
    if d[i]>mx:
        mx=d[i]
        sm=mx
    else:
        continue
print(sm)
        
    

    
