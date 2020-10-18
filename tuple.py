from collections import namedtuple
n=int(input())
x,y,z,k=input().split()

student=namedtuple('student',(x,y,z,k))
s=0
for i in range(0,n):
    a,b,c,d=input().split()
    student(a,b,c,d)
    if x=='MARKS':
        s=s+int(a)
    if y=='MARKS':
        s=s+int(b)
    if z=='MARKS':
        s=s+int(c)
    if k=='MARKS':
        s=s+int(d)
        
g=s/n
print('{:.2f}'.format(g))
