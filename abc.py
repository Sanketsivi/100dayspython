questions=[['1.Which is not a prime number.',7,9,5,2,2] ,
    
    ["2.What is the capital India?","Mumbai","Delhi","Kolkata","Bhopal",3],
    
    ['3.Which is not a prime number.',7,9,5,2,2] ,
    
    ["4.What is the capital India?","Mumbai","Delhi","Kolkata","Bhopal",3],
    
    ['5.Which is not a prime number.',7,9,5,2,2] ,
    
    ["6.What is the capital India?","Mumbai","Delhi","Kolkata","Bhopal",3]]


prize=[1000,2000,3000,5000,10000,20000,50000,120000,250000,320000]
win=0
for i in range(0,len(questions)):
    question=questions[i]
    print(f"\n\n{questions[i][0]}") 
    print(f'''1.{question[1]}             2.{question[2]}
3.{question[3]}              4.{question[4]}'''
          )
    ans=int(input("Enter the value from (1-4),0 for quit:"))
    if ans==0:
        print("You quit! You won",prize[i-1])
    
    if ans==question[-1]:
        print("You answer is Correct! You won ",prize[i])
        if i==4:
         win=1000
        elif i==9:
          win==320000
    else:
        print('Your answer is wrong!You won ',win)
        break
