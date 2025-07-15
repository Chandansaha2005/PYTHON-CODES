#WAP  to swap two values using tuple assignment
a=int(input("Enter the 1st no. = "))#10
b=int(input("Enter the 2nd no. = "))#20
print(f"Before swap A = {a} and B = {b}")
a,b=b,a
print(f"After swap A = {a} and B = {b}")