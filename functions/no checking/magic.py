#Magic No.
def magic(n):
    s=0
    while(n>0):
        s+=n%10
        n//=10
        if n==0:
            if s==1:
                return True
            elif s<10:
                return False
            else:
                n=s
                s=0 
n=int(input("Enter the no. ="))
if magic(n):
    print("Magic no.")
else:
    print ("Not Magic No.")