#WAP to read a character until * is encountered using while loop.Also count the number of uppercase,lowercase and numbers entered by the users
print("Press '*' to stop")
l=0
u=0
d=0
s=0
while True:
    n=input("Enter the character = ")
    n=n[0]
    if n=='*':
        break
    else:
        if n.islower():
            l+=1
        elif n.isupper():
            u+=1
        elif n.isnumeric():
            d+=1
        else:
            s+=1
print("Total Upper case : ",u)
print("Total Lower case : ",l)
print("Total Numerics : ",d)
print("Total Special Characters : ",s)