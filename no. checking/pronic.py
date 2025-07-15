#Pronic No.
n=int(input("Enter the no. = "))
for i in range(1,n+1):
    if n==i*(i+1):
        print("Pronic no.")
        exit()
print("Not Pronic no.")