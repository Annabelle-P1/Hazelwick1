hours=-1
total=0
while hours != 0:
    hours=int(input("Enter hours:"))
    choice=input("is your car is electric:")   
    if choice == "yes":
        total=hours*2
    else:
        total=hours*4
    print(total)
