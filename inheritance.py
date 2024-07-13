class student:
    def __init__(self,name,marks):
        self.marks=marks
        self.name=name
    
    def info(self):
        print(f"Marks of {self.name} is {self.marks}")

x=student("asvi",89)
x.info()
