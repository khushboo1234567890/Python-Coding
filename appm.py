# check whether a character is:

#Uppercase, lowercase, digit or special character

n = input("Enter a character: ")

if n.isupper():
    print("The character is uppercase.")
elif n.islower():
    print("The character is lowercase.")
elif n.isdigit():
    print("The character is a digit.")
else:
    print("The character is a special character.")


