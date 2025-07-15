#Acromatic string
x=input("Enter the String = ")
x=x.upper()
j=0
print("String = ",x)
for i in range(0,len(x),1):
    if i==0:
        print(x[i],end="")
    elif x[i]==' ':
        print(".",end="")
        print(x[i+1],end="")
        j=i
j+=2
x=x.lower()
for i in range(j,len(x),1):
    print(x[i],end="")