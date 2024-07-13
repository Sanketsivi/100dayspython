from functools import lru_cache
import time
 
@lru_cache(maxsize=None)
 
def func(n):
    print("hello")
    time.sleep(4)
    return n

print(func(2))
print(func(3))
print(func(4))
print(func(2))
print(func(5))