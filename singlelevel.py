class Parents:
    def __init__(self,name,occupation):
        self.name=name
        self.occupation=occupation
    def showdet(self):
        print(f"My name is {self.name} and I am {self.occupation}")
    def hello(self):
        print(f"hello {self.name}")

class Child(Parents):
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def showdetChild(self):
        print(f"My name is {self.name} and my age is {self.age}")

p=Parents("Abc","developer")
c=Child("edf",21)
p.showdet()
c.showdetChild()
#c.showdet()--> it will through error because ocupation is not present in child
c.hello()
