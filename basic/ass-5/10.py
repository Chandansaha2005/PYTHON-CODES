# 1/1 + 1/4 + 1/9 + ... + 1/n**2
n=int(input("Enter the range = "))
s=0
for i in range(1,n+1):
    print(1,"/",i**2,end="   ")
    s+=1/i**2
print()
print("Sum = ",s)