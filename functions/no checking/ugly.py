#Ugly No.
def factor(n):
    f=[]
    x=n
    li=[2,3,5]
    i=2
    while(i<=n):
        if n%i==0:
            n//=i
            f.append(i)
        else:
            i+=1
    print("Factors of",x,"is :",f)
    for i in f:
        if i not in li:
            print("Not Ugly No.")
            exit()
    print("Ugly No.")
n=int(input("Enter the no. = "))
factor(n)