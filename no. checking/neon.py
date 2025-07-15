#Neon no.
n=int(input("Enter the no. = "))
s=0
x=n**2
while(x!=0):
    s+=x%10
    x//=10
if s==n:
    print("Neon No.")
else:
    print("not Neon No.")