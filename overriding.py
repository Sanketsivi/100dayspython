class A:
    def hello():
        print("hello I am in class A")
    name="sivi"
    def show(self):
        print(f"My name is {self.name}")

class B(A):
    def hello():
        print("Hye I am in class B")
    
a=A()
a.show()

b=B
b.hello()

