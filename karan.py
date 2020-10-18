x = int(input())
y = int(input())
z = int(input())
n = int(input())
g=[]
h=[]
#we have to make the list of three inntegers
for i in range(0,x+1):
    for j in range(0,y+1):
        for k in range(0,z+1):
            if n!=i+j+k:
                g=[i,j,k]
                h.append(g)
print(h)
            
