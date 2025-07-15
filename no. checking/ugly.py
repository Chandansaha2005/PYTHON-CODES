#ugly no.
n=int(input("Enter the no. = "))
while n!=1:
    if n%2==0:
        n//=2
    elif n%3==0:
        n//=3
    elif n%5==0:
        n//=5
    else:
        print("Not Ugly No.")
        exit()
print("Ugly no.")
