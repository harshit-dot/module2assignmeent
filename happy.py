class rectangle:
    def __init__(self,l,b,r):
        self.length=l
        self.bredth=b
        self.radius=r
    def area_rectangle(self):
        a=self.length*self.bredth
        print(a)
    def area_circle(self):
        p=self.radius*3.14
        print(p)
a=int(input('enter the value of length'))
b=int(input('enter the value of breadth'))
c=int(input('enter the value of radius'))
p1=rectangle(a,b,c)
p1.area_rectangle()


    
        
