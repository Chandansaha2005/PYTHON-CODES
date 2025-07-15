#WAP o calculate the sum of values in a list using the reduce function().
import functools
li=[]
n=int(input("Enter the range = "))
for i in range(n):
    li.append(int(input("Enter the no. = ")))
print(li)
sum=functools.reduce(lambda a,b:a+b,li)
print("Sum of the elements of the list is :",sum)