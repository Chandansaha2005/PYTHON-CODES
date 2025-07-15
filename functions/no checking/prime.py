def prime(x):
    for i in range(2,x):    
        if x%i==0:
            return False
    return True        
n=int(input("Enter the No. = "))
if prime(n):# func. calling
    print(n,"is Prime")
else:
    print(n,"is NOT Prime")