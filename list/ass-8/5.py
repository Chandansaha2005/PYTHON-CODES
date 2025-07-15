#WAP to illustrate the use of enumerate() to print an individual item and its index in the list
li=[]
n=int(input("Enter the range = "))
for i in range(n):
    li.append(int(input("Enter the no. = ")))
print(li)
for i,j in enumerate(li):
    print("value at ",i,"index is :",j)