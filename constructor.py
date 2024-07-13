class info:
    def __init__(self,name,profession) :
        self.name=name
        self.profession=profession
    def details(self): 
        print(f"My name is {self.name} and by profession I am {self.profession}")

x=info("sanket","software developer")
print(x.name)
x.details()

        