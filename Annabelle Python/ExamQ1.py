c=0
while c<=8:
    hight =int(input("Enter your hight in cm:"))
    if hight <= 140 and hight >= 120:
        q=input("Are you with an adult:")
        if q== "yes":
            print("You are allowed to ride!")
            c=c+1
        else:
            print("you are not allowed!")
    elif hight >= 140:
        print("you are alowed to ride")
        c=c+1
    else:
        print("your are allowed to ride")
        print("Ride is full go away")