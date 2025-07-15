#delete an element within a list
li=[]
li2=[]
n=int(input("Enter the Range = "))
for i in range(0,n,1):
    li.append(int(input("Enter the No. = ")))
print("List = ",li)#10,20,10,30,10
x=int(input("Enter the No. to be searched for = "))#10
for i in li:#i=10
    if i==x:
        li.remove(i)   #20,30
print(li)