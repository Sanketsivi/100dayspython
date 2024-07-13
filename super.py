class Parent:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def show(self):
        print(self.name)
class Child(Parent):
    def __init__(self,name,age,lan):
        super().__init__(name,age)
        self.lan=lan
    
p= Parent("shjh",21)
a=Child("akj",21,"py")
print(p.name)
print(a.name)