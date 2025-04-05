################### Generate a Bill #################

Bill=float(input("Enter The Bill:"))
people=int(input("Enter the number of People:"))
tip=int(input("Enter the tip 10%,15%,or 12%:"))
Fill_Bill=(tip/100*Bill+Bill)/people
print(round(Fill_Bill,2))
