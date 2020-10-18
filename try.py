n=int(input())
lst=[]
for i in range(0,n):
    a,b=input().split()
    d=[a,b]
    lst.append(d)
for i in lst:
    k=i[0]
    l=i[1]
    try:
        if int(l)>0 and int(k)>0:
            s=int(k)//int(l)
            print(s)
        if int(l)==0:
             print('Error Code: integer division or modulo by zero')

    except:
        if ord(k)>=34 and ord(k)<=45:
            print('Error Code: invalid literal for int() with base 10:', "'{}'".format(k))
        else:
            print('Error Code: invalid literal for int() with base 10:', "'{}'".format(l))

            
    

    

