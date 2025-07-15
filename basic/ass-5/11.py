# 1/2 + 2/3 + 3/4 + ... + n/n+1
n=int(input("Enter the range = "))
s=0
for i in range(1,n+1):
    print(i,"/",i+1,end="   ")
    s+=i/i+1
print()
print("Sum =",s)