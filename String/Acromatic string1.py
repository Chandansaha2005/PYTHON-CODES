#Acromatic string
x=input("Enter the String = ")
x=x.upper()
print("String = ",x)
for i in range(0,len(x),1):
    if i==0:
        print(x[i],end="")
    elif x[i]==' ':
        print(".",end="")
        print(x[i+1],end="")