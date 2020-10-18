n=input()
d=int(input())
k=len(n)//d
al=[]
for i in range(0,k):
    lst=[]
    for j in range(0,d):
        lst.append(n[j+d*i])
        
    al.append(''.join(lst))
las=[]
print(al)
for i in range(0,len(al)):
    se=[]
    for j in al[i]:
        se.append(j)
    las.append(se)
print(las)
for i in las:
    kar=set()
    for j in i:
        if j not in kar:
            print(j,end='')
            kar.add(j)
    print()
