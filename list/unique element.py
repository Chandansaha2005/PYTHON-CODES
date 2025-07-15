#copy the unique element from one list to another list
li=[]
li2=[]
n=int(input("Enter the Range = "))
for i in range(0,n,1):
    li.append(int(input("Enter the No. = ")))
print("List = ",li)
for i in li:
    if i not in li2:
        li2.append(i)
print("Copy List = ",li2)
li2[2]=""
print("Copy List = ",li2)