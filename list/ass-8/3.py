#Write a python program to combine and print elements of two list using list comprehension.
n=int(input("Enter the range = "))
li1=[]
li2=[]
for i in range(n):
    li1.append(int(input("Enter the no. of list 1 = ")))
    li2.append(int(input("Enter the no. of list 2 = ")))
print(li1)
print(li2)
li=list((x,y) for x in li1 for y in li2)
print(li)