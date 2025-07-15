#Neon No.
def check(n):
    x=n**2
    s=0
    while x>0:
        s+=x%10
        x//=10        
    return s
n=int(input("Enter the no. = "))
if n==check(n):
    print("Neon No.")
else:
    print("Not Neon No.")