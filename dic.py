class Employee:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def show(self):
        print(f"name is:{self.name}")

e=Employee("sanket",20)
print(e.__dict__)#-- dict is use to represent the variable in the form of dictionary
print(help(Employee))#-- help tell us about any string ,class or method