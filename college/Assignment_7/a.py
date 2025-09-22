def fibo_n(n=1):
    return n if n < 2 else fibo_n(n-1) + fibo_n(n-2)

n = int(input("Enter n for fibo_n(): ") or 1)
print(f"{n}-th Fibonacci number is:", fibo_n(n))