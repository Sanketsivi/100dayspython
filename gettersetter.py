class team:
    def __init__(self,p1,p2):
        self.p1=p1
        self.p2=p2
    @property
    def rundet(self):
        print(f"Player 1 score:{self.p1}")
    @rundet.setter
    def rundet(self,new):
        self.p1=new

x=team(45,56)
print(x.p1)
x.rundet=57
x.rundet
