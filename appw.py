# find the factorial of a number.
number = int(input("Enter a number: "))
factorial = 1
if number < 0:
    print("Factorial is not defined for negative numbers.")
elif number == 0 or number == 1:
    print(f"The factorial of {number} is 1.")
else:
    for i in range(2, number + 1):
        factorial *= i
    print(f"The factorial of {number} is {factorial}.")

    