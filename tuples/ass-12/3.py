#WAP to print nested elements of tuples using for loop
t=((10,20),(20,30),(30,40),(40,50))
for i in t:#i=(10,20)
    for j in i:#j=10
        print(j,end=" ")
    print()
    