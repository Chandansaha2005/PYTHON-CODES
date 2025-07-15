#WAP to print m-n no. and specify as odd and even
m=int(input("Enter the starting no. = "))
n=int(input("Enter the ending no. = "))
if m%2==0:
    print("\tEven\t\tOdd")
    for i in range(m,n+1):
        if i%2==0:
            print("\t",i,end="\t")
        else:
            print("\t",i)
else:
    print("\tOdd\t\tEven")
    for i in range(m,n+1):
        if i%2==1:
            print("\t",i,end="\t")
        else:
            print("\t",i)