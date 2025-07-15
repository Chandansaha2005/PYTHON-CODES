#WAP to show the string formatting function with tuple
t=()
n=int(input("Ente the range = "))
for i in range (n):
    t+=(int(input("Enter the value : ")),)
    print("My tuple : ",t)
for i in range(n):
    print(f"The value at {i} index is {t[i]}")