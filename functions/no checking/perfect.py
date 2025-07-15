#Perfect No.
def factor(n):
    s=0
    for i in range(1,n):
        if n%i==0:
            s+=i
    return s
n=int(input("Enter the no. = "))
if n==factor(n):
   print("Perfect No.") 
else:
    print("Not Perfect no.")
