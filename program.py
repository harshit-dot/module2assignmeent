def solve(n):
    k=n.split()
    g=[]
    h=[]
    for i in k:
        p=i[0].upper()
        k=i.replace(i[0],p)
        g.append(k)
 
    for i in g:
        m=[]
        for j in i:
            m.append(j)
            for k in range(1,len(m)):
                m[k]=m[k].lower()
        s=''.join(m)
        h.append(s)
    z=' '.join(h)

    return z
            



s = input()

result = solve(s)

print(result)    

            
            
            
                   
    
        
        
        
    

    

        
    

