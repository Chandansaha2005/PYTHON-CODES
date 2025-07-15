#WAP to concatenate two strings using + operator,append a string using += operator, repeat a string using * operator.
print("PRESS \n'+' For concatenate 2 string\n'+=' For append a string into another\n'*' For repeat a string multiple times\n'#' to exit")
while True:
    c=input("Enter the choice = ")
    if c=='+':
        a=input("Enter the 1st string = ")
        b=input("Enter the 2nd string = ")
        print(a+" "+b)
    elif c=='+=':
        a=input("Enter the 1st string = ")
        b=input("Enter the 2nd string = ")
        a+=b
        print(a)
    elif c=='*':
        a=input("Enter the string = ")
        b=input("Enter the no of times the string will multiply = ")
        print(a*b)
    else :
        print("Invalid Input")
        break