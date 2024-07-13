a=10
print(a:=11)

b=False
print(b:=True)

books=list()
# while True:
#   book=input("Enter the book u want to enter")
#   if book=="end":
#    break
#   books.append(book)
# print(books)

# using walrus
while (book:=input("Enter the book u want to enter"))!="quit":
    books.append(book)