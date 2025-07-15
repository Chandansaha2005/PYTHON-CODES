#Karpekar no.
def check(n):
    sq=n**2
    c=len(str(n))
    if n==(sq%(10**c))+(sq//10**c):
        return True
    else:
        return False
n=int(input("Enter the no. = "))
if check(n):
    print("Karpekar no.")
else:
    print("Not Karpekar No.")