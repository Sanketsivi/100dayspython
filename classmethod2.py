#class method as constructor
class Student:
    def __init__(self,name,rn):
        self.name=name
        self.rn=rn
    def show(self):
        print(f"name:{self.name} and rollno:{self.rn}")
    @classmethod
    def strfrom(cls,string):
        return cls(string.split("-")[0],string.split("-")[1])
        
string="SAnket-21"

s=Student.strfrom(string)
s.show()