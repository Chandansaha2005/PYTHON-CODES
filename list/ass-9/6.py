#WAP to remove all duplicates from a list
li,li2=[],[]
n=int(input("Enter the range = "))
for i in range(n):
    li.append(int(input("Enter the no. :")))
print(li)
for i in li:
    if i not in li2:
        li2.append(i)
print(li2)
