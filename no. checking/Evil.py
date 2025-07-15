#Evil No.
n=int(input("Enter the no. = "))
x=n
s=""
c=0
while (n>0):
    s+=str(n%2)
    if n%2==1:
        c+=1
    n//=2
s=int(s[::-1])
print("Binary Equivalent of ",x,"is : ",s)
if c%2==0:
    print(x,"is Evil no.")
else:
    print(x,"is Not Evil No.")