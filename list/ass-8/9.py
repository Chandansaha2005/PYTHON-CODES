#Write a python program to pass more than one sequence to the map() function
n=int(input("Enter the range = "))
li1=[]
li2=[]
for i in range(n):
    li1.append(int(input("Enter the no. of list 1 = ")))
print()
for i in range(n):
    li2.append(int(input("Enter the no. of list 2 = ")))
print(" ",li1)
print("+",li2)
li3=list(map(lambda x,y:x+y,li1,li2))
print("------------------------------")
print(" ",li3)