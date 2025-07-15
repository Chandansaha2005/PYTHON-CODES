#ugly no.
def check(n):
    while n!=1:
        if n%2==0:
           n//=2 
        elif n%3==0:
            n//=3
        elif n%5==0:
            n//=5
        else:
            return False
    return True
n=int(input("Enter the no. = "))
if check(n):
    print("Ugly No.")
else:
    print("Not Ugly No.")