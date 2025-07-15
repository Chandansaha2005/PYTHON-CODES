#Spy no.
n=int(input("Enter the no. = "))
s=0
p=1
x=n
while(n!=0):
    s+=n%10
    p*=n%10
    n//=10
if s==p:
    print("Spy No.")
else:
    print("not Spy No.")