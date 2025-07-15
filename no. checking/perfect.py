#Perfect No.
n=int(input("Enter the no. = "))
s=0
for i in range(1,n):
    if n%i==0:
        s+=i
if s==n:
    print("Perfect No.")
else:
    print("not Perfect No.")