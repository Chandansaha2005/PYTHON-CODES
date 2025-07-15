#delete an element within a list
li=[]
n=int(input("Enter the Range = "))
for i in range(0,n,1):
    li.append(int(input("Enter the No. = ")))
print("List = ",li)#10,20,30,40,50
c=0
x=int(input("Enter the No. to be Searched for = "))#20
for i in range(0,n,1):
    if li[i]==x:
        c=1
        del(li[i])
        print(li)
        break
if c==0:
    print(x,"Not Found")