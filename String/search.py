#WAP to check the presence of a given character
li=input("Enter the string = ")
x=input("Enter the character that is to be searched : ")
li=li.lower()
x=x.lower()
c=0
for i in li:
    if x==i:
        c+=1
        print(x,"is present at ",c,"index")
    else:
        c+=1
        