#WAP to take input into a list and sort it
li=[]
n=int(input("Enter the range = "))
for i in range(0,n):
    li.append(int(input("Enter the no. = ")))
print("Unsorted List = ",li)
li.sort()
print("Sorted List = ",li)