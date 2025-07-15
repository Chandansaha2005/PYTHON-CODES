#Sum of digit of a no.
n=int(input("Enter the no. = "))
x=n
s=0
while(n>0):
    s+=n%10
    n//=10
print("Sum of digit of",x,"is :",s)