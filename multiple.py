class A:
    def hello():
        print("Hello I am A")
class B(A):
    def hye():
        print("Hye I'm B and i have properties of A")
class C(A):
    def bye():
        print("Bye everyone by the way I have also properties of A")

a=A
b=B
c=C
a.hello()
b.hye()
b.hello()
c.bye()
c.hello()
#c.hye()-- IT WILL THROUGH ERROR BECAUSE C DONT HAVE HYE FUNCTION AND IT NOT HAVE B PROPERTIES