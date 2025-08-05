n=int(input("Enter the Range = "))
for i in range(n):
    print("  "*(n-i-1),end="")
    for j in range (i,-1,-1):
        print(chr(65+j),end=" ")
    print()