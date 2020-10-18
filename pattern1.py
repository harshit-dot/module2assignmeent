n=int(input())
m=int(input())
a=(n-1)//2
b=(m-1)//2
f=m-7
k=f//2

for i in range(0,a):
    for j in range(0,b-(3*i)-1):
        print(end='-')
    for j in range(0,(2*i)+1):
        print('.|.',end='')
    for j in range(0,b-(3*i)-1):
        print(end='-')
    print()
for i in range(0,1):
    for j in range(0,k):
        print(end='-')
    for j in range(0,1):
        print('WELCOME',end='')
    for j in range(0,k):
        print(end='-')
    print()
for i in range(0,a):
    for j in range(0,(3*i)+3):
        print(end='-')
    for j in range(0,n-(2*i)-2):
        print('.|.',end='')
    for j in range(0,(3*i)+3):
        print(end='-')
    print()

