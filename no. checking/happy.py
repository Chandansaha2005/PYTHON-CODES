#Happy No.
n=int(input("Enter the no. = "))
x=str(n)
while True:
    s=0
    for i in x:
      s+=int(i)**2
    if s==1:
        print("HAPPY NO.")
        exit()
    elif s!=1 and s<10:
        print("Not Happy No.")
        exit()
    else:
        x=str(s)