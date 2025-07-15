#Co prime no.
def prime(x):
    for i in range(2,x):
        if x%i==0:
            return False
    return True
n=int(input("Enter the 1st no. = "))
m=int(input("Enter the 2nd no. = "))
while m>0:
    r=n%m
    n=m
    m=r
if n==1 and prime(n) and prime(m):
    print("Co-Prime No.")
else:
    print("not Co Prime")