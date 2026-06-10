# Palindrome 
a = input("Enter a string: ")

if a == a[::-1]: 
    print("palindrome")
else:
    print("not palindrome")

a = int(input("Enter a number: "))
if a == int(str(a)[::-1]):
    print("palindrome") 
else:
    print("not palindrome")