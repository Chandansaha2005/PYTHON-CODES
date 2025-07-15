#WAP to store the positive and negative list element in 2 diff lists
li=[]
pos=[]
neg=[]
c=0
n=int(input("Enter the range = "))
for i in range(0,n):
    li.append(int(input("Enter the no.= ")))
print("List = ",li)
for i in li:
    if i>0:
        pos.append(i)
    elif i<0:
        neg.append(i)
    else:
        c+=1
print("Positive List = ",pos)
print("negative List = ",neg)
print("No. of zero = ",c)