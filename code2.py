a ,b ,c=input().split()
a=int(a)
b=int(b)
c=int(c)
lst=[]
lst.append(a)
lst.append(b)
lst.append(c)
d,e,f=input().split()
d=int(d)
e=int(e)
f=int(f)
lste=[]
lste.append(d)
lste.append(e)
lste.append(f)
m1 , n1=input().split()

m1=int(m1)
n1=int(n1)
aa=m1*n1
lst0=[]
lst0.append(m1)
lst0.append(n1)

m2 , n2=input().split()

m2=int(m2)

n2=int(n2)
bb=m2*n2
lst1=[]
lst1.append(m2)
lst1.append(n2)
m3 , n3=input().split()

m3=int(m3)
n3=int(n3)
cc=m3*n3
lst2=[]
lst2.append(m3)
lst2.append(n3)
t=int(input())
j=max(lst)
lst3=[]
lst3.append(aa)
lst3.append(bb)
lst3.append(cc)
index=0
for i in range(0,len(lst)):
    if lst[i]==j:
        index=i
x=j*lst3[index]
l=min(lst)
for i in range(0,len(lst)):
    if lst[i]==l:
        index1=i
y=lste[index1]*l
for i in lst:
    if i==j or i==l:
        continue
    index2=i
z=index2*(t-lst3[index]-lste[index1])
total=x+y+z
print(total)

