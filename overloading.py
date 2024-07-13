class Rec:
    def __init__(self,len,bre):
        self.len=len
        self.bre=bre
    def area(self):
        return self.len*self.bre
class Circle(Rec):
    def __init__(self,radius):
        self.radius=radius
        super().__init__(radius,radius)

    def area(self):
        return 3.14*super().area()

r=Rec(56,67)
print(r.area())
c=Circle(10)
print(c.area())

