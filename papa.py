n=int(input())
k=[]
d=dict()
for i in range(0,n):
    name,a,b,c=input().split()
    k=[a,b,c]
    d[name]=k
query_name=input()
l=0
for i,j in d.items():
    if i==query_name:
        for s in j:
            l=l+float(s)
        q=l/3
print("{:.2f}".format(q));
    
    
    

        
