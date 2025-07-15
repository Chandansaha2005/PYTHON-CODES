# 1 + 1/2 + 1/3 + 1/4 + ... + 1/n
n=int(input("Enter the range = "))
s=0
for i in range(1,n+1):
    print(1,"/",i,end="   ")
    s+=1/i
print()
print("Sum =",s)