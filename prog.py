s=input()
a=0
b=0
c=0
k=0
for i in s:
    if i.isalnum():
        d=d+1
for i in s:
    if i.isalpha():
        c=c+1
for i in s:
    if i.isdigit()==True:
        k=k+1

    
for i in s:
    if i.islower()==True:
        a=a+1
        
for i in s:
    if i.isupper()==True:
        b=b+1
if d==0:
    print('False')
else:
    print('True')
if c==0:
    print('False')
else:
    print('True')
if k==0:
    print('False')
else:
    print('True')
if a==0:
    print('False')
else:
    print('True')
if b==0:
    print('False')
else:
    print('True')
    

        
        

