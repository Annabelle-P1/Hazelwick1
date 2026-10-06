minutes=int(input("Enter a number of minutes:"))
hours = minutes // 60
remaining_minutes = minutes % 60
print(f"{minutes} minutes is {hours} hour and {remaining_minutes} minute.")