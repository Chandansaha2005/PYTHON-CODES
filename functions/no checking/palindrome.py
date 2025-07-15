#Palindrome no. 
def reverse(n):
    return int(str(n)[::-1])
n=int(input("Enter the no. = "))
if n==reverse(n):
    print("Palindrome no.")
else:
    print("Not Palindrome no.")