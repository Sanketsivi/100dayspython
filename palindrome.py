a=int(input("Enter a number:"))
temp=a
rev=0
while(a!=0):
    r=a%10
    rev=rev*10+r
    a=a//10

if(rev==temp):
    print(temp,"is a palindrome number.")
else:
    print(temp,"is not a palindroe number")