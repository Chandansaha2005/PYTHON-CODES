#WAP to illustrate nesteed list
list1=[]
list2=[]
m=int(input("Enter the lists = "))
for i in range(0,m):
    n=int(input("Enter the range = "))
    for i in range (0,n):
        list1.append(int(input("Enter the no. : ")))
    print(list1)
    list2.append(list1)
    list1=[]
print(list2)