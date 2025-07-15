# 1/1 + 4/2 + 9/3 + ... + n**2/n
n=int(input("Enter the no. = "))
s=0
for i in range(1,n+1):
    print(i**2,"/",i,end="   ")
    s+=i**2/i
print()
print("Sum =",s)