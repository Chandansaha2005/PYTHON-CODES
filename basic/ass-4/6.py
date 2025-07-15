#WAP to binary number to equivalent decimal number using while loop
n=int(input("Enter the binary no. = "))
x=n
n=int(str(n)[::-1])
c=len(str(n))
s=0
while n!=0:
    s+=(n%10)*2**(c-1)
    c-=1
    n//=10
print("decimal of ",x,"is :",s)