#WAP to enter a decimal number. Calculate and display the binary equivalent of this number using while loop
n=int(input("Enter the no. = "))
x=n
s=''
while(n!=0):
    s=s+str(n%2)
    n//=2
s=s[::-1]
print("Binary Equivalent of ",x,"is :",s)