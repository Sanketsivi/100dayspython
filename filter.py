def cube(a):
    return a>6
lis=[5,4,87,9,6,8]
#filter functon return the value in list those who return the true in function
new=list(filter(cube,lis))
print(new)