# 30. check wether a given day number (1-7) croresponds to  a weekday or weekend.
day = int(input("Enter a day number (1-7): "))

if 1 <= day <= 5:
    print("The day corresponds to a weekday.")
else:
    print("The day corresponds to a weekend.")