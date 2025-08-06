import math
a=float(input("Enter the value of a = "))
b=float(input("Enter the value of b = "))
c=float(input("Enter the value of c = "))

d=b*b-4*a*c

if(a!=0):
    if(d>0):
        r1=(-b+math.sqrt(d))/(2*a)
        r2=(-b-math.sqrt(d))/(2*a)
        print("Real and Different Roots = ",r1,"and",r2)
    elif(d==0):
        root = -b/(2*a)
        print("Real an Equal Roots = ", root)
    else:
        print("Roots are Imaginary")
else:
    print("Not a Quadratic Equation")
