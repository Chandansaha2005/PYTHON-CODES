#Palindrome No.
n=int(input("Enter the no. = "))
if n==int(str(n)[::-1]):
    print("Perfect No.")
else:
    print("not Perfect No.")