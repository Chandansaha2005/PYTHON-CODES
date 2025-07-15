#Armstrong No.
n=int(input("Enter the no. = "))    #153
x=n
c=len(str(n))                       #3
s=0
while(n!=0):
    s+=(n%10)**c
    n//=10
if s==x:
    print("Armstrong No.")
else:
    print("not Armstrong No.")
