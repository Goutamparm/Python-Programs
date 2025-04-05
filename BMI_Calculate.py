############ BMI ##################

weigth=float(input("Enter the weight kg:"))
height=float(input("Enter the number meter:"))
Bmi=weigth/(height**2)

if Bmi<18.5:
    print("under Weight")
elif Bmi>=18.5:
    print("normal Weight")
elif Bmi>=25:
    print("over weight")
else:
    print("Error")
