score = 0

answer = int(input("What is 7 + 5? "))
if answer == 12:
    print("Correct!")
    score += 1
else:
    print("Wrong! The answer was 12.")

answer = int(input("What is 15 - 8? "))
if answer == 7:
    print("Correct!")
    score += 1
else:
    print("Wrong! The answer was 7.")

answer = int(input("What is 6 * 4? "))
if answer == 24:
    print("Correct!")
    score += 1
else:
    print("Wrong! The answer was 24.")

answer = float(input("What is 20 / 5? "))
if answer == 4:
    print("Correct!")
    score += 1
else:
    print("Wrong! The answer was 4.")

final_score = score * 5 / 4

print("You scored", final_score, "out of 5.")