#Lambda function is use to create a function in single line.It is anonymous 
#function means that function is without name
cube=lambda x:x**3
print(cube(3))
sum=lambda x,y,z:x+y+z
print(sum(7,8,9))

#we can use also use function as an arguement in function
def func(fx,value):
    return fx(value)
 
print(func(cube,3))