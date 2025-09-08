#WAP to return the highest as well as the lowest values in the list
x=input("Enter the nos. using ',' : ")
t=tuple(x.split(','))
print(t)
print("Max =",max(t))
print("Min =",min(t))