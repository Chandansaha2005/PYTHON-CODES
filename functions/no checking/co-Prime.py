def gcd(a, b):#a=15,b=8
    while b>0:#0>0
        rem=a%b#rem=0
        a=b#a=1
        b=rem#b=0
    return a
def is_prime(n):
    for i in range(2,n):
        if n % i == 0:
            return False
    return True
a = int(input("Enter the 1st No. = "))#15
b = int(input("Enter the 2nd No. = "))#8
if gcd(a, b) == 1 and is_prime(a) and is_prime(b):
    print("Co Prime Numbers")
else:
    print("Not Co Prime Numbers")