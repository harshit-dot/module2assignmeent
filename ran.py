n=int(input())
k=4*(n-1)-1
for i in range(0,n-1):
    for j in range(0,2*(n-i-1)):
        print(end='-')
    for j in range(0,(2*i)+1):
        print('*',end='-') 
    for j in range(0,2*(n-i-1)-1):
        print(end='-')
    print()
for j in range(0,1):
    for i in range(0,k//2+2):
        print('*',end='')
        if i==k//2+1:
            break
        print(end='-')
    print()


for i in range(0,n-1):
    for j in range(0,(2*i)+2):
        print(end='-')
    for j in range(0,(2*(n-i-1)-1)):
        print('*',end='-') 
    for j in range(0,(2*i)+1):
        print(end='-')
    print()


