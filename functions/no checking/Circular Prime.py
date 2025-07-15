#Circular Prime
def is_prime(n):
    for i in range(2,n):
        if n % i == 0:
            return False
    return True
def circulate(n):
    s = str(n)
    return int(s[1:] + s[0])
n=int(input("Enter the no. = "))
a = n
while True:
    print(a)
    if is_prime(a)==False:
        print(n," IS NOT A CIRCULAR PRIME")
        exit()
    a = circulate(a)
    if a==n:
        break
print(n," IS A CIRCULAR PRIME")
        
'''
try:
    n = int(input("Enter a number: "))
    is_circular_prime(n)
except ValueError:
    print("Invalid input. Please enter a valid integer.")
'''