#WAP to count an element within a list(linear search)
li=[]
n=int(input("Enter the Range = "))
for i in range(0,n,1):
    li.append(int(input("Enter the No. = ")))
print("List = ",li)
j=0
x=int(input("Enter the No. to be searched = "))
for i in li:
    if i==x:
        j=j+1
if j>=1:
    print(x,"present",j,"Times")
else:
    print(x,"Not Found")