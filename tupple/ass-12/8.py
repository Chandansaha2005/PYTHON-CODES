#WAP that accepts different number of arguments and return sum of only the positive values passed to it
li,n,s=[],int(input("Enter the range = ")),0

for i in range(n):
    x=int(input("Enter the values : "))
    li.append(x)
    if x>0:
        s+=x

print("My List : ",li)
print("SUM of Postive no. : ",s)