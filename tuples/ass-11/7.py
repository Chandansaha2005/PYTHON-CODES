#WAP to demonstrate the use of nested tuples
x=input("Enter the nos. of tuple 1 using ',' : ")
t1=tuple(x.split(','))
y=input("Enter the nos. of tuple 2 using ',' : ")
t2=tuple(y.split(','))
t3=(t1,)+(t2,)
print(t3)
t4=t1+t2
print(t4)