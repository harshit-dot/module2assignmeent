no=int(input())
for j in range(1,no+1):
    z=j
    n=j
    r=j
    lst=[]
    lst1=[]
    lst2=[]
    print(n,end='  ')
    while z!=0:
        p=z%8
        z=z//8
        lst1.append(p)
  
  
  
  
   
  
        
    q=len(lst1)
    for i in range(0,q):
       
        print(lst1[q-i-1].rjust(spacing=' ')
              
    while r!=0:
        s=r%16
        r=r//16
        if s==10:
            lst2.append('A')
        elif s==11:
            lst2.append('B')
        elif s==12:
            lst2.append('C')
        elif s==13:
            lst2.append('D')
        elif s==14:
            lst2.append('E')
        elif s==15:
            lst2.append('F')
        else:
            lst2.append(s)
    k=len(lst2)
    for i in range(0,k):
        print(lst2[k-i-1].rjust(spacing=' '))


   
    while n!=0:
        s=n%2
        n=n//2
        lst.append(s)
    k=len(lst)
    for i in range(0,k):
        print(lst[k-i-1],end='')
    print()
   
