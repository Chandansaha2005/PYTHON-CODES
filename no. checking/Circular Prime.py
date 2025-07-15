#Circular Prime
n=int(input("Enter the no. = "))
a=n
while True:
    print(a)
    for i in range(2,a):
        if a%i==0:
            print("Not Circular Prime no.")
            exit()
    s=str(a)
    a=int(s[1:]+s[0])
    if a==n:
        print("Circular Prime No.")
        exit()