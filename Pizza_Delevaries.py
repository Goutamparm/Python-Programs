############## Pizza Delevaries ####################

size=input("Enter the Pizza Size S,M or L:")
pepperoni=input("Enter the Pepperoni in Pizza Y or N:")
extra_cheese=input("Enter the Extra Chesse Y or N:")
price=0

if size=="S":
    price=15
    print("small $",price)

elif size=="M":
    price=20
    print("Medium $", price)

elif size=="L":
    price=25
    print("Large $",price)

if pepperoni == "Y":
    if size == "S":
        price += 2
    else:
        price += 3

if extra_cheese=="Y":
    price += 1

    finalBill=price
    print(finalBill)

else:
    print("Wrong Input")
