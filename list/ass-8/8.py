#WAP that adds 2 to every value in the list using map() function 
n=int(input("Enter the range = "))
li=list(range(1,n+1))
print(li)
li2=list(map(lambda x:x+2,li))
print(li2)