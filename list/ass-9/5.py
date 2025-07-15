#WAP that forms a list of first character of every word in another list
li,li2=[],[]
n=int(input("Enter the range :"))
for i in range(n):
    li.append(input("Enter the Name :"))
print(li)
for i in li:
    li2.append(i[0])
print(li2)