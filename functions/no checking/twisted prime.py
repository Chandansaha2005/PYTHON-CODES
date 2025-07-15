#Twisted prime no.
def prime(n):
    for i in range(2,n):
        if n%i==0:
            return False
    return True
n=int(input("Enter the no. = "))
x=str(n)
x=int(x[1:]+x[0])
if prime(n)and prime(x):
    print("Twisted Prime")
else:
    print("Not Twisted Prime")