class hello:
    def __init__(self,name,age):
        self.__name=name #__ is use to make any variable private and _ use for make any variable protected
        self._age=age
    def info(self):
        print(f"My name is {self.__name}")

x=hello("sanket",10)
#print(x.__name)--> it will through error because we cannot acccess private variable directly
print(x._hello__name)#-> we can access it indirectly 
print(x._age)
print(dir(hello))
