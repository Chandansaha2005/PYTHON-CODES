n=int(input("Enter the Nth term = "))
a,b=0,1
for i in range (n):
    print(a,end=" ")
    temp = a+b
    a,b=b,temp
    