#WAP to count the no. of space in a string
x=input("Enter the string = ")
c=0
for i in x:
    if i==' ':
        c+=1
print("Total no. of spcae in",x,"is",c)