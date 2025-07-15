#Prime No.
n=int(input("Enter the no. = "))
for i in range(2,n):
    if n%i==0:
        print(n,"is not prime no.")
        exit()
print(n,"is prime no.")