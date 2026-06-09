# 29. Determine whether a student gets a scholarship (marks >= 85 and attendance >75%)

marks = int(input("Enter your marks: "))
attendance = int(input("Enter your attendance percentage: "))

if marks >= 85 and attendance > 75:
    print("Congratulations! You have received a scholarship.")

else:
    print("Sorry, you do not qualify for a scholarship.")