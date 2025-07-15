#WAP that has a nested list to store toppers details.Edit the details and reprint the details.
def print_values(t,sub):
    li=['Name','Marks','City']
    s=0
    print(f"Details of the Topper".center(20,'-'))
    for i in range(len(t)):
        if i==1:
            for i in range(len(sub)):
                s+=int(t[1][i])
                print(f"{li[1]}  in {sub[i]} : {t[1][i]}") 
            print("Total Marks  :",s)
        else:
            print(f"{li[i]}  : {t[i]}")  
            

t_li,li=[],[]
t_li.append((input("Enter the name of the Topper : ")).title())
sub=(input("Enter the name of subjects using ',' : ")).split(",")
for i in range(len(sub)):
    x=int(input(f"Enter the marks of {sub[i].title()} : "))
    li.append(x)
c=input("Enter the city : ")
print()
t_li.append(li)
t_li.append(c.title())
print_values(t_li,sub)
print()


print("PRESS to change\n1 : Name\n2 : Marks\n3 : City\n4 : Exit")
while True:
    i=int(input("Enter the choice : "))
    if i==1:                    #Name Change
        t_li[0]=(input("Enter the Name : ")).title()
    elif i==2:                  #Marks Change
        for i in range(len(sub)):
            x=int(input(f"Enter the marks of {sub[i].title()} : "))
            li.append(x)
        t_li[1]=li
    elif i==3:                  #City Change
        t_li[2]=(input("Enter the City : ")).title()
    else:
        print("After all Changes...")
        print_values(t_li,sub)
        exit()

