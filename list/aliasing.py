#WAP to show aliasing of a list and uses of sort() method.
l1=[]
n=int(input("Enter the range = "))
for i in range(0,n):
    l1.append(int(input("Enter the no. = ")))
l2=l1
print(l1)
l2.sort()
print(l1)