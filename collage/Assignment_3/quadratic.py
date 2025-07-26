import math
a=float(input("Enter the value of a = "))
b=float(input("Enter the value of b = "))
c=float(input("Enter the value of c = "))

d=b*b-4*a*c

if(a!=0):
    if(d>0):
        r1=(-b+math.sqrt(d))/(2*a)
