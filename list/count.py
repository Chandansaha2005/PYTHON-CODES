#WAP to check the presence of a given character
li=input("Enter the string = ")
x=input("Enter the character that is to be counted : ")
li=li.lower()
x=x.lower()
c=0
for i in li:
    if x==i:
        c+=1
if c>=1:
    print(x,"is present",c,"times in",li,)