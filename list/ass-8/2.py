#Write a python program to find cubes of a list using list comprehension
n=int(input("Enter the range = "))
li=list(range(1,n+1))
li2=list(i**3 for i in li)
print(li2)