############## Welcome Treasure Island Game ###############

print("Welcome to Treasure Island\nYour mission is to find Treasure")
side=input("Where you go Left or right:")
if side=="Left" :
    swim_or_wait=input("Where you go Swim and Wait:")
    if swim_or_wait=="Wait":
        door = input("Which Door You Open Red ,Blue or Yellow:")
        if door == "Yellow":
            print("You win")
        else:
            print("Game Over")
    else:
        print("Game over")


else:
    print("Game Over")
