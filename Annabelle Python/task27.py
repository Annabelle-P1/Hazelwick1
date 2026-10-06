temperature=int(input("Enter a number in celcius"))
if temperature<0:
    print("Freezing")
elif temperature<20:
    print("Cold")
elif temperature<30:
    print("Warm")
elif temperature>30:
    print("Hot")