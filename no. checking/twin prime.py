#Twin prime no.
def is_prime(n):
    for i in range(2,n):
        if n%i==0:
            return False
    return True
n=int(input("Enter the 1st no. = "))
m=int(input("Enter the 2nd no. = "))
if is_prime(n) and is_prime(m) and abs(n-m)==2:
    print("Twin Prime No.")
else:
    print("Not Twin Prime No.")