#Write a program to enter a decimal number. Calculate and display the binary equivalent of this number using while loop
n=int(input("Enter the no. = "))
x,s=n,''
while n!=0:
    s+=str(n%2)
    n//=2
print(f"Binary Equivalent of {x} is {int(s[::-1])}")
