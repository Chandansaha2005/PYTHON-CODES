#WAP that takes user name and PAN card number as input.Validate the information using isX() function and print the details.
user_name = input("Enter the user name : ")
Pan_no = input("Enter the Pan No.   : ") 
u=user_name.upper()
p=Pan_no.upper()
c=''
for i in range(0,len(u)):
    if u[i]==' ':
        c=u[i+1]
print("User Name :",u ,"\nPan No.   : ",p)
if p[0:5].isalpha() and p[4]==c and p[5:9].isnumeric():
    print("Valid input")
else:
    print("InValid input")
     
