#WAP to illustrate the use of zip() function
li,li2=[],[]
n=int(input("Enter the range : "))
for i in range(n):
    li.append(int(input("Enter the value at list 1 : ")))
    li2.append(int(input("Enter the value at list 2 : ")))
print("List 1 :",li)
print("List 2 :",li2)
t=()
for i in zip(li,li2):
    t+=(i,)
print(t)