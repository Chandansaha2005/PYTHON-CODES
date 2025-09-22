prime = lambda x: x>1 and all(x%i for i in range(2, int(x**0.5)+1))
primes = list(filter(prime, range(251, 5501)))[::-1]

print("Prime numbers between 251–5500 (reverse):")
print(primes)