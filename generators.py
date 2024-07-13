def mygenerators():
  for i in range(5):
    yield i

gen=mygenerators()
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))

#second way
for a in gen:
  print(a)

  

  