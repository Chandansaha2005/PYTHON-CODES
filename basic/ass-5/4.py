#WAP to check prime no.
n=int(input("Enter the no. = "))
for i in range(2,n):
    if n%i==0:
        print("Not Prime No.")
        exit()
print("Prime No.")