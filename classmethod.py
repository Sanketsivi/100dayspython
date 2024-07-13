class Employee:
    company= "Google"
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def show(self):
        print(f"Employee name is {self.name} and age is:{self.age} and working in {self.company}")

    def changecom1(self,new1):
        self.company=new1

    @classmethod #--> class method is use to change the value of class variable
    def changecom(self,new):
        self.company=new

e=Employee("sanket",12)
e.show()
e.changecom1("Flipkart")#--this will not change the class variable value bcz class method is not used
print(Employee.company)
e.changecom("Microsoft")
print(Employee.company)#--class method used
