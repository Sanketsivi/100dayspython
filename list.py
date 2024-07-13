


list=[3,4,"sanket",'abc',8.0,87,45,"jain"]
list1=[3,4,8.0,87,1,45.7,3,5]
print(list)
print(list[0])


y=list1.index(3,3,8)
print(y)

list1.sort()
print(list1)

c=list1.count(3)
print(c)

list1.remove(4)
print(list1)

print("negative\n")
print(list[-2])
print(list[len(list)-2])
print(list[8-2])

print("\njump")
print(list[1:8])
print(list[1:8:2])
print(list[1:8:3])


lst= [i*i for i in range(5)]
print(lst)
lst1= [i*i for i in range(8) if (i%2==0)]
print(lst1)

if "sanket" in list:
    print("yes")

else:
    print("no")
  