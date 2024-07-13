class team:
    def __init__(self,name,jno):
        self.name=name
        self.jno=jno
    def showdet(self):
        print(f"Player name is {self.name} and its jersey no. is{self.jno}")
    @staticmethod
    def addrun(a,b):
        return a+b

ply=team("rohit",45)
ply.showdet()
print(team.addrun(56,76)) #-->static method doesnt need any object for call