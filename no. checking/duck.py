#Duck No.
n=input("Enter the no. = ")
x=int(n)
if n[0]=='0':
    print(n,"is not a duck no.")
else:
    for i in n:
        if i=='0':
            print(n,"is a duck no.")
            exit()
    print(n,"is not a duck no.")