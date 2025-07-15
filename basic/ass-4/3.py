#WAP to check given number is Armstrong number or not using while loop
n=int(input("Enter the no. = "))
x=n
c=len(str(n))
s=0
while(n!=0):
   s+=(n%10)**c
   n//=10
if s==x:
    print("Armstrong no.") 
else:
    print("Not Armstorng No.")