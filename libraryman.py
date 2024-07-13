books=[]
no_of_books=0
while(True):
   print('''   1.For check books in library
   2.For add book in library
   3.Check no. of books in library
   0.Exit''')
   press=int(input("Press key(1-3,0 for exit):"))
   if press==1:
      print(f"Books present--{books}")
      print("\n")
   
   elif press==2:
      n=int(input("No. of books u want to include:"))
      for i in range(n):
       addbook=input("Enter the book you want to include:")
       books.append(addbook)
       for i in range(no_of_books):
        if addbook==books[i]:
           print("Book already present in library!")
           break
        
       no_of_books+=1
       print("Book added successfully!")
       print("\n")
   
   elif press==3:
       print(f"Total no. of books:{no_of_books}") 
       print("\n")
   elif press==0:
      break
   else:
      print("Press correct") 

print("Thank You! ")



