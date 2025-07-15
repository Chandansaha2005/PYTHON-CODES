#WAP to use id()
n=int(input("Enter the range = "))
li=[]
for i in range(n):
    li.append(int(input("Enter the no. = ")))
print(li)
print("Id of the list is = ",id(li))