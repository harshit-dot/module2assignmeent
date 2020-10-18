from math import *
a=int(input())
b=int(input())
d=sqrt((a*a)+(b*b))

c=d/2

angle=asin(c/b)

g=degrees(angle)

m=chr(176)
print(round(g),end='')
print(m)

