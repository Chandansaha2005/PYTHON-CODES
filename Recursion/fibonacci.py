#fibonacci recursion
def fibo(n):#n=2
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return fibo(n-1)+fibo(n-2) #1+1+3
    
n=int(input("Enter the Range = "))#n=5
for i in range(n):
    print(fibo(i),end=" ")