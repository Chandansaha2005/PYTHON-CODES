#WAP to calc. the average of 1st n no.
n=int(input("Enter the range = "))
s=0
for i in range(1,n+1):
    s+=i
print("Average of 1 to",n,"is :",s/n)