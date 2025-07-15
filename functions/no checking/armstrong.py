#Armstrong no.
def check(n,c):
    s=0
    while(n>0):
        s+=(n%10)**c
        n//=10
    return s
n=int(input("Enter the no.= "))
c=len(str(n))
if n==check(n,c):
    print("Armstrong no.")
else:
    print("Not Armstrong No.")