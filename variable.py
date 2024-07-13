x=10
print(x)
def variable():
    global z
    z=15
    y=11
    print(f"Value of local variable is:{y}")
    print(x)
    print(z)

print(f"Value of global variable:{x}")
variable()
#print(z)-->it will through error because z is local variable it is accesible only inside within function
#to change the local variable into global variable we use "global" keyword
print(f"Converting local to global variable value:{z}")