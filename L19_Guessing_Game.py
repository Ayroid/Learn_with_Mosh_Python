# Code which gives user 3 chances to guess a secret number

num = 9
i=1
ctr=0
while(i<=3):
    guess=input("Guess: ")
    if(int(guess)==num):
        print("You Win!")
        break
    else:
        ctr+=1
    i+=1
if(ctr==3):
    print("You Loose")
