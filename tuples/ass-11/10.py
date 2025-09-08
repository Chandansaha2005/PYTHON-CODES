#WAP to count the no. of times 'x' is present into a string
nm=input("Enter the names separated by ',' :")
t=tuple(nm.split(","))
x=input("Enter the character to search for :")
for i in t:
    c=0
    if x in i:
        c=i.count(x)
        print(x,"Is present in",i ,c,"times")
    else:
        print(x,"Is not present in",i)