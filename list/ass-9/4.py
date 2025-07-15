#WAP to print index at which a particular value exists.If the value exists at multiple locations in the list,then print all the indices.Also count the number of times that value is repeated in the list
li=[]
n=int(input("Enter the range : "))
for i in range(n):
    x=int(input("Enter the no. = "))
    li.append(x)
print("List : ",li) 
x=int(input("Enter the no. to be searched :"))
if x in li:
    print(f"{x} is present {li.count(x)} at ",end="")
    for i in range(n):
        if li[i] == x:
            print(i,end=" ")
    print("indexes")
else:
    print(f"{x} not found")