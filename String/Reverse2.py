#WAP to reverse  a string
x=input("Enter the String = ")
print("String = ",x)
print("Reverse String = ",end="")
for i in range(len(x)-1,-1,-1):
    print(x[i],end="")