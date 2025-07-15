#WAP to calc the factorial of a no. 
n=int(input("Enter the no. = "))
f=1
print("Factorial of",n,"is :",end=" ")
for i in range(1,n+1):
    f*=i
    if i==n:
        print(i,end=" = ")
        break
    print(i,end="*")
print(f)