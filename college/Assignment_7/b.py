def fibo_s(n=1, a=0, b=1, res=[]):
    if n == 0: return res
    return fibo_s(n-1, b, a+b, res+[a])

n = int(input("Enter n for fibo_s(): ") or 1)
print(f"Fibonacci series up to {n} terms:", fibo_s(n))