#WAP to print the reverse of a number and using while loop
n=int(input("Enter the no. = "))
x=n
s=0
while n>0:
    s=s*10+n%10
    n//=10
print("Reverse of ",x,"is :",s) 