import time
init=time.time()
print(init)
j=0
for i in range(5):
    print(i)

print(time.time() - init)

while j<5:
    print(j)
    j=j+1
print(time.time() - init)