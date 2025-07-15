#WAP to calc.  the sum and mean of a list
import functools
li=[]
n=int(input("Enter the range = "))
for i in range(n):
    li.append(int(input("Enter the no. = ")))
print(li)
s=functools.reduce(lambda a,b:a+b,li)
print("Sum = ",s,"\nMean = ",s/n)  