class Student:
    schoolname="A.A.P.S." #--Class variable
    def __init__(self,name,age):
        self.name=name  #-->instance variable
        self.age=age
    def showdet(self):
        print(f"Student name:{self.name} ,age:{self.age} and school name:{self.schoolname}")

s1=Student("sanket",21)
s2=Student("neha",22)
s1.showdet()
Student.schoolname="saroj"

print(Student.schoolname)
s1.showdet()
#Student.showdet(s1)
s2.schoolname="Hope"
s2.showdet()
print(Student.schoolname)

