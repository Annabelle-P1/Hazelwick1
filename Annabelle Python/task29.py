length1=float(input("Enter a length:"))
length2=float(input("Enter a length:"))
length3=float(input("Enter a length:"))
if length1 == length2 == length3:
    print("The triangle is equilateral")
elif length1 == length2 or length1 == length3 or length2 == length3:
    print("The triangle is isosceles")
else:
    print("The triangle is scalene")