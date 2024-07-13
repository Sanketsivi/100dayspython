class Employee:
    name="sanket"
    sur="jain"
    def __len__(self):
        i=0
        for a in self.name:
            i=i+1
        return i
    def __str__(self):
        return f"hello kese hoo"
    def __repr__(self):
        return "badiya" 
    def __call__(self):
        print( "someone is calling u")
        
e=Employee()
print(e)
print(len(e))
print(repr(e))
e() #-calling call method