#WAP to count the no. of prime and non prime no. given by the user until user press '-1'
print("Press '-1' to stop")
c=0
c1=0
while True:
    f=0
    n=int(input("Enter the no. = "))
    if n==-1:
        break
    else:
        for i in range(2,n):
            if n%i==0:
                f=1
                break
        if f==1:
            c+=1
        else:
            c1+=1
print("No. of prime nos. : ",c1)
print("No. of non prime nos. : ",c)