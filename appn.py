# Determine the ticket price

age = int(input("Enter your age: "))
if age < 12:
    print("Child ticket is 100.")
elif age >= 12 and age < 59:
    print("Adult ticket is 200.")
else:
    print("Senior ticket is 150.")