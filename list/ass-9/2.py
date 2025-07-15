#WAP using filter function to a list of squares of numbers form 1..10.Then use the for..in construct to sum the elements in the list generated
li=list(map(lambda x: x**2 ,range(1,11)))
print(li)
s=0
for i in li:
    s+=i
print("Sum = ",s)