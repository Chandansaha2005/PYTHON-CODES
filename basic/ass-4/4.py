#WAP o read the numbers until -1 is encountered. Find the average of positive and negative numbers entered by the user using while loop.
print("Press '-1' to stop")
s=0
c=0
while True:
    n=int(input("Enter the no. : "))
    if n==-1:
        break
    else:
        s+=n
        c+=1
print("Average = ",s/c)