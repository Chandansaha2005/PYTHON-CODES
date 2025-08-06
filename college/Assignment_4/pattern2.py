n=int(input("Enter the Range = "))
for i in range (1,n):
    print("*"*i)
print("*"*(2*n-1))
for j in range(n-1,0,-1):
    print(f'{"*"*j:>{(2*n-1)}}')