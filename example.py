shoes=int(input())
size=input().split()[:shoes]
print(size)
    
buy=int(input())
lst=[]

for i in range(0,buy):
    a,b=input().split()
    g=[int(a),int(b)]
    lst.append(g)
print(lst)
sm=0
print(sm)
for i in lst:
    d=lst[0]
    for j in size:
        if d==int(j):
            size.remove(j)
            sm=sm+i[1]
        

print(size)
print(sm)
            
            

    
    



    
