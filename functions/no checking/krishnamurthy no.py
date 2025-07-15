#Krishnamurty No.
def krishnamurthy(n):
    x=n
    s=0
    while(n>0):                             #n=0
        rem=n%10                            #rem=1
        f=1
        for i in range(1,rem+1):
            s+=f                            #145
        n//=10                          #n=0
    if(x==s):
        print(x," is Krishnamurthy No. ")
    else:
        print(x," is NOT Krishnamurthy No. ")
n=int(input("Enter the No. = "))
krishnamurthy(n)#calling