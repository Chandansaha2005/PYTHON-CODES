#sum of digit of a no.
def sod(n):#n=0
    if n==0:
        return n
    return n%10+ sod(n//10)#4+3+2+1+0=10
n=int(input("Enter the No. = "))#n=1234
print("Sum of Digit = ",sod(n))