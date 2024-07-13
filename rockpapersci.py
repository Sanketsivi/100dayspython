import random
print("WELCOME TO THE WORLD OF RPS GAME")
print("Enter\n 1 for Rock\n 2 for Paper\n 3 for Scissors")
choose=int(input("Choose b/w (1-3):"))
ran=random.randint(1,3)

if choose>3:
     print("Please enter correct option")
     

else:
    if(choose==2 and ran==1):
     print("You Win!")
    elif(choose==1 and ran==3):
     print("You Win!")
    elif(choose==3 and ran==2):
     print("You Win!")
    elif(choose==ran):
     print("Match Drawn!")
    else:
     print("You loose!")
         
