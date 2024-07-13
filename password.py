import random
character="ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890~!@#$%&*()_+:?><,./;"
password=""
length=int(input("Enter the length of password:"))
for i in range(length):
    password+=random.choice(character)

print(password)