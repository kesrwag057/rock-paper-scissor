
import random
moves = ["Rock","Paper","Scissors"]

keep_playing = "true"

while keep_playing=="true":
    cmove =random.choice(moves)
    pmove = input("Please enter your choice:")
    print("The computer chooses:",(cmove))


    if cmove==pmove:
        print("Tie")

    else:
        print("please enter the correct value")

    if pmove=="Paper" and cmove=="Rock":
        print("You wins")
    

    if pmove=="Rock" and cmove=="Paper":
        print("Computer Wins")

    if pmove=="Paper" and cmove=="Scissors":
        print("Computer wins")
        

    if pmove=="Scissors" and cmove=="Paper":
        print("You Win")
    

    if pmove=="Rock" and cmove=="Scissors":
        print("You win")
    

    if pmove=="Scissors" and cmove=="Rock":
        print("Computer Wins")
    
