def sum_of_digit(n):
    s=0
    while(n>0):
        s+=n%10
        n//=10
    print(s)
    return s
def factor(n):
    s=0
    i=2
    while (n>1):
        if n%i==0:
            s+=sum_of_digit(i)
            n//=i
        else:
            i+=1
    return s
n=int(input("Enter the no. = "))
if sum_of_digit(n)==factor(n):
    print("Smith No.")
else:
    print("not Smith No.")