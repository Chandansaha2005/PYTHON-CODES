#Pronic no.
def pronic(n):
    for i in range(1,n+1):
        if n==i*(i+1):
            return True
    return False
n=int(input("Enter the no. = "))
if pronic(n):
    print("Pronic no.")
else:
    print("not Pronic no.")