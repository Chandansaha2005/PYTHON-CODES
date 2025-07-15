#Disarium no.
def check(n,c):
    s=0
    while(n>0):
        s+=(n%10)**c
        c-=1
        n//=10
    return s
n=int(input("Enter the no.= "))
c=len(str(n))
if n==check(n,c):
    print("Disarium no.")
else:
    print("Not Disarium No.")