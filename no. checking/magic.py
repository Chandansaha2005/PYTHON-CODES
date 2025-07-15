#Magic No.
n=int(input("Enter the no. = "))
s=0
while(n>0):
    s+=n%10
    n//=10
    if n==0:
        if s==1:
            print("Magic no.")
        elif s!=1 and s<10:
            print("Not Magic no.")
        else:
            n=s
            s=0