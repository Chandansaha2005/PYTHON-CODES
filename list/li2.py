#WAP to take input into a list and print it
li=[]
n=int(input("Enter the range = "))
for i in range(0,n):
    x=int(input("Enter the no. = "))
    li.append(x)
print("list = ",li)
for i in li:
    print(i,end=" ")