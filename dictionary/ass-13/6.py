#WAP to randomly pop() or remove an element from a dictionary
x={1:10,2:20,3:30,4:40,5:50}
print(x)
n=int(input("Enetr the key to be deleted = "))
print("deleted value at",n,"is ",x[n])
x.pop(n)
print(x)
