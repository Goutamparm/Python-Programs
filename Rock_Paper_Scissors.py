################## Rock,Paper,Scissor Game ##################
import random

choice1=["Rock","Paper","Scissor"]
choice2=["Rock","Paper","Scissor"]

random_choice1=random.choice(choice1)
random_choice2=random.choice(choice2)

if random_choice1=="Rock" and random_choice2=="Scissor":
    print("you Win")
elif random_choice1=="Scissor" and random_choice2=="Paper":
    print("you Win")
elif random_choice1=="Paper" and random_choice2=="rock":
    print("You Win")
elif random_choice1==random_choice2:
    print("Draw match")
else:
    print("You Lose","Computer Wins")
