import random
class welcome:
    def __init__(self) -> None:
        
        print("WELCOME TO BANK MANAGEMENT SYSTEM")
class info:
    def __init__(self,name,age,dob,password):
        self.name=name
        self.age=age
        self.dob=dob
        self.password=password
    def show(self):
        print("Your account has been opened successfully")
        print(f"Name:{self.name}\n" 
              f"Age:{self.age}\n"
              f"DOB:{self.dob}\n"
              f"Password:{self.password}"
              f"Account no:{random.randint(1,100000)}")

    
w=welcome()

while True:
#   have to start open
  name=input("Enter your name:")
  age=int(input("Enter your age:"))
  dob=(input("Enter your dob"))
  passw=input("Enter your password")
  i=info(name,age,dob,passw)
  i.show()
  

