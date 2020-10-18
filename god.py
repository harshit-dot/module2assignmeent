n=int(input())
c=[]
k=[]
g=[]
for i in range(0,n):
    name=input()
    no=float(input())
    c=[name,no]
    k.append(c)
for i in k:
    g.append(i[1])
h=min(g)
for i in k:
    if h==i[1]:
        print(i[0])
for i in g:
    if h==i:
        g.remove(i)
f=min(g)
for i in k:
    if f==i[1]:
        print(i[0])

        
    


    
    
