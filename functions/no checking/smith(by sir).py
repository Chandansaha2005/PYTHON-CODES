import math
def prime_factors(n):
    factors = []
    while n % 2 == 0:
        factors.append(2)
        n //= 2
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        while n % i == 0:
            factors.append(i)
            n //= i
    if n > 2:
        factors.append(n)
    return factors

def sod(n):
    s = 0
    while n > 0:
        rem = n % 10
        s += rem
        n //= 10
    return s

def smith(n):
    factors = prime_factors(n)
    last_factor_sod = sod(factors[-1])
    total = sum(factors) + last_factor_sod
    return total
n = int(input("Enter the number: "))
sum_of_digit = sod(n)
sum_of_factors = smith(n)
print("Sum of factors =", sum_of_factors)
if sum_of_digit == sum_of_factors:
    print("The number is a Smith number")
else:
    print("The number is not a Smith number")