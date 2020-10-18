n=int(input())
m=input().split()[:n]
o=int(input())
d=[]
for i in range(0,o):
    a,b=input().split()
    c=[int(a),int(b)]
    d.append(c)
print(d)
lst=[]
for i in d:
    g=i[0]
    f=i[1]
    print(g)
    print(f)
    for j in m:
        if g==int(j):
            lst.append(f)
            m.remove(j)
            print(lst)
            print(m)
            break
s=0           
for i in lst:
    s=s+i
print(s)
    
            
        
