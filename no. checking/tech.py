#Tech no.
n=int(input("Enter the no. = "))
c=len(str(n))
s=0
if c%2==0:
    c//=2
    s=n%10**c+n//10**c
    if s**2==n:
        print("Tech No.")
    else:
        print("Not Tech No.")
else:
    print("Not Tech No.")