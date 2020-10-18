n=int(input())
k=[]
z=[]
g=input()
k=g.split()
for i in range(0,n):
    k[i]=int(k[i])
z=z+k
for i in range(0,n):
    if k[i]==1:
        k[i]='one'
    if k[i]==2:
        k[i]='two'
    if k[i]==3:
        k[i]='three'
    if k[i]==4:
        k[i]='four'
    if k[i]==5:
        k[i]='five'
    if k[i]==6:
        k[i]='six'
    if k[i]==7:
        k[i]='seven'
    if k[i]==8:
        k[i]='eight'
    if k[i]==9:
        k[i]='nine'
    if k[i]==0:
        k[i]='zero'
    
p=[]
for i in k:
    for j in range(0,len(i)):
        p.append(i[j])
q=0
for i in p:
    if i == 'a' or i=='e' or i=='i' or i=='o' or i=='u':
        q=q+1
m=0
for i in range(0,len(z)):
    for j in range(i+1,len(z)):
        if z[i]+z[j]==q:
            m=m+1
if m==1:
    print('one')
if m==2:
    print('two')
if m==3:
    print('three')
if m==4:
    print('four')
if m==5:
    print('five')
if m==6:
    print('six')
if m==7:
    print('seven')
if m==8:
    print('eight')
if m==9:
    print('nine')
if m==0:
    print('zero')

