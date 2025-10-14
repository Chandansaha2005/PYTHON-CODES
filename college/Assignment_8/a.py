import numberCheck

num = int(input("Enter an integer: "))
if numberCheck.is_prime(num): 
    print(f"{num} is a Prime number.")
else: 
    print(f"{num} is not a Prime number.")
    
if numberCheck.is_palindrome(num):
    print(f"{num} is a Palindrome number.")
else:
    print(f"{num} is not a Palindrome number.")