#WAP to sort keys in a dictionary
x={}
n=int(input("Enter the range = "))
for i in range(n):
    k=int(input("Enter the Key : "))
    x[k]=int(input("Enter the value : "))
print(x)
print(dict(sorted(x.items())))