#Karpekar no.
n=int(input("Enter the no. = "))
sq=n**2
s=0
c=len(str(n))
s=sq%10**c+sq//10**c
if n==s:
    print("Karpekar no.")
else:
    print("Not Karpekar No.")