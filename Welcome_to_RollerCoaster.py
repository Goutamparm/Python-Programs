############# Welcome to RollerCoaster ##############

height =int(input("Enter the Height in CM:"))

if height>120:
    print("can Ride")
    age=int(input("Enter the age:"))
    if age<=12:
        price=5
        print("Give $5")
    elif age>12 and age<=18:
        price=7
        print("Give $7")
    elif age>18:
        price=12
        print("Give $12")
    elif age>=45 and age<=55:
        print("Free Ride")
        photos=str(input("you want photo Y or N:"))
        if photos=="Y":
           photos=3
           print("Photos $3")
        else:
           print("No Photos")
        finalBill = price + photos
        print(f"FinalBill:${finalBill}")
else:
    print(f"Can't Ride")
