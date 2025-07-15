#Factor of a no.
n=int(input("Enter the no. = "))
i=1
print("Factor of ",n,"is ",end=" = ")
while(n!=1):
    if n%i==0:
        print(i,end=" ")
        n//=i
        if i==1:
            i+=1
    else:
        i+=1