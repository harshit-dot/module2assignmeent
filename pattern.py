n=int(input())
m=int(input())
k=(m-1)//2
for i in range(0,n):
    for j in range(0,k-i-1):
        print(end='-')
    for j in range(0,(2*i)+1):
        print('.|.',end='')
    for j in range(0,k-i-1):
        print(end='-')
    print()
