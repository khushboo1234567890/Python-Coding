n = 123456
c=n
rev = 0
while n%10:
    rev = rev*10 + n%10
    n = n//10

print(rev)  

if c== rev:
    print("palindrome") 
else:
    print("not palindrome")