a=9
b=9
print(a is b)
#is  check the location of object in memory
#here a and b has same value so they place in same memory location and they are immutable(not change)
print(a==b)
#== check the value
x=[1,2,3]
y=[1,2,3]
#here x and y has same value but they do not  place in same memory location because x and y is list and list is muttable
print(a==b)
print(x is y)
print(x==y)