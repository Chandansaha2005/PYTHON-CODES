#WAP to print the 1st index of all the element within a list
li=[]
n=int(input("Enter the Range = "))
for i in range(0,n,1):
    li.append(input("Enter the String = "))
print(li)
for i in li:
    print(i[0],end="")
