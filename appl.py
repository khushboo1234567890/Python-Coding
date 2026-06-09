# calculate bonus

salary = int(input("Enter your salary: "))

if salary > 50000:
    print("You get a bonus of 20%")

elif salary > 30000 and salary <= 50000:
    print("You get a bonus of 10%")
else:
    print("You get a bonus of 5%")