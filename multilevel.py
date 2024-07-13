class Cat:
    def __init__(self,name,voice):
      self.name=name
      self.voice=voice
    def show(self):
       print(f"Hey I'm cat and my voice is mew-mew ")
class Dog(Cat):
   def __init__(self,name,voice):
      self.name=name
      self.voice=voice
   def show(self):
       Cat.show(self)
       print(f"Hey I am dog and my voice is bhau-bhau")
class Animal(Dog):
    def __init__(self,name,voice):
      self.name=name
      self.voice=voice
    def show(self):
       Dog.show(self)
       print(f"Hey I'm {self.name} and my voice is {self.voice}")
a=Animal("a",23)
d=Dog("sheru","bhau-bhau")
c=Cat("merry","mew-mew")
a.show()


