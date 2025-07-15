#Harshad no.
n=int(input("Enter the no. = "))
s=0
for i in str(n):
    s+=int(i)
if n%s==0:
    print("Harshad no.")
else:
    print("Not Harshad no.")