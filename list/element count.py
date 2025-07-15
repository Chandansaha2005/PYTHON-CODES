#WAP to count each element within a list
li=[]
n=int(input("Enter the Range = "))
for i in range(0,n,1):
    li.append(int(input("Enter the No. = ")))
print("List = ",li)
j=-98123
for i in li:
    x=li.count(i)
    if x==1:
        print(i,"present",li.count(i),"No. of Times")
    elif x>1 and j!=i:
        print(i,"present",li.count(i),"No. of Times")
        j=i