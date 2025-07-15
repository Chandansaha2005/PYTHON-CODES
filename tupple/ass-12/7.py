#WAP that has a list of numbers(both positive as well as negative).Make a new tuple that has only positive values from this list
li,n=[],int(input("Enter the range = "))

for i in range(n):
    li.append(int(input("Enter the values : ")))
print("My List : ",li)

t=tuple(filter(lambda x: x>0 , li))#li=[-1, -8, 70, -8, -5]
print("Positive tuple : ",t)