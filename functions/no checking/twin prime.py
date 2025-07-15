def is_prime(n):
    for i in range(2,n):
        if n%i==0:
            return False
    return True
n1 = int(input("Enter the 1st No. = "))#n1=4
n2 = int(input("Enter the 2nd No. = "))#n2=7
if is_prime(n1) and is_prime(n2) and abs(n1 - n2) == 2:
    print("Twin Prime")
else:
    print("Not Twin Prime")