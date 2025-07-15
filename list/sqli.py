#WAP to find the sum of squares of all elements in a list using filter()
def square(x):
    return x**2
n=int(input("Enter the range = "))
my_list=list(range(1,n+1))
s=0
x=list(map(square,my_list))
print(x)
for i in x:
    s=s+i
print("Sum = ",s)