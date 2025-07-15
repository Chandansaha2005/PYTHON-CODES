#Write a python program to make a list of cubes.
n=int(input("Enter the range = "))
li=list(range(1,n+1))
li2=list(map(lambda x:x**3,li))
print(li2)