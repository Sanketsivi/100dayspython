from functools import reduce
def sum(x,y):
    return x+y
lis=(9,87,7,65,8)
#reduce func take the value and put in into function and then return it in list
new=(reduce(sum,lis))
print(new)