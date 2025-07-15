#Twisted prime
def is_prime(n):
    for i in range(2,n):
        if n%i==0:
            print("Not Twisted prime no.")
            return False
            exit()
    return True
n=int(input("Enter the NO.  = "))
x=n
s=str(n)
n=int(s[1:]+s[0])
if is_prime(x) and is_prime(n):
    print("Twisted Prime")
