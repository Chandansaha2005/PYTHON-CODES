#WAP to calculate GCD of two numbers using while loop
def gcd(a,b):
    i=1
    p=1
    while(i<=b):
        if a%i==0 and b%i==0:
            p*=i
            a//=i
            b//=i 
            if i==1:
                i+=1
        else:
            i+=1
    return p    
n=int(input("Enter the 1st no. : "))
m=int(input("Enter the 2nd no. : "))
if n>m:
    x=gcd(m,n)
elif m>n:
    x=gcd(n,m)
print("GCD of ",n,"and",m,"is :",x)