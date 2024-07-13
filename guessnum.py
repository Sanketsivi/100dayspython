import random
print("________________WELCOME TO GAME________________")
print("You have guess the no. b/w 0-100 and you have 10 chances for guessing")
#guess=int(input("Guess the number:"))
com=(random.randint(0,100))
i=0
count=1
while i<=5:
    
    guess=int(input("Guess the number:"))
    
    if(guess==com):
        print("You guess the Correct number!")
        
        print(f"You guess the number in {count} chance")
        
        break
    else:
        print("You guess Wrong number.Try Again!")
        count+=1
    i+=1
    if i==5:
        print("Gameover")
        break