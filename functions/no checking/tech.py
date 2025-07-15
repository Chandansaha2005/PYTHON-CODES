#Tech no.
def check(n,c):
    x=n%10**c+n//10**c
    if x**2==n:
        return True
    else:
        return False
n=int(input("Enter the no. = "))
c=len(str(n))
if c%2==0:
    c//=2
    if check(n,c):
        print("Tech no.")
    else:
        print("not Tech No.")