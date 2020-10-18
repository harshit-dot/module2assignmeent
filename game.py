
name=input()
g=[]
cou=0
cow=0
for i in range(0,len(name)):
    g.append(name[i])
d='harshdvdjhjbjedgiehdidihe'
kl='hscgecugcjgrcug'
for i in range(0,len(g)):
    if d==g[i]:
        continue
    
    
    h=g[i]
    k=[]
    lst1=[]
    lst3=[]
    
    if h=='A' or h=='E' or h=='I' or h=='O' or h=='U':
        d=h
        for j in range(i,len(g)):
            
            k.append(g[j])
            p=''.join(k)
            kal=name.count(p)
            cou=cou+kal+3

        
        
for i in range(0,len(g)):
    if d==g[i]:
        continue
    h=g[i]
    k=[]
    lst2=[]
    lst=[]
    if h!='A' and h!='E' and h!='I' and h!='O' and h!='U':
        d=h
        for j in range(i,len(g)):
            k.append(g[j])
            p=''.join(k)
            pal=name.count(p)
            cow=cow+pal
if cow>cou:
    print('Stuart', cow)
else:
    print('Kevin', cou)
            
            
            
            
    
        
    
