#WAP  to sort a tuple of values
t,n=(),int(input("Enter the range : "))
for i in range (n):
    t+=(int(input("Enter the Value : ")),)
print("Before sorting : ",t)
p=sorted(t)
print("After sorting : ",p[::-1])