def sod(n):#n=0
    if n==0:
        return n
    return n%10+ sod(n//10) #10
def check(n):#n=10
    x= sod(n)#10
    if x<10:
        return x
    else:
        return check(x)
n = int(input("Enter the No. = "))#n=181
if check(n)==1:
    print(n,"is a Magic No.")
else:
    print(n,"is not a Magic No.")