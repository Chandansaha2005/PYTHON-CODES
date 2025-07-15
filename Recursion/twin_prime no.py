#Wap to check two numbers are twin prime or not
def is_prime(n,i):#7,0,7
    if  i==1:
        return True
    else:
        if n%i==0:
            return False
        return is_prime(n,i-1)#2
num=int(input("Enter The 1st Number : "))#5
num2=int(input("Enter The 2nd Number : "))#7
if is_prime(num,num-1) and is_prime(num2,num2-1) and abs(num-num2)==2:
    print(f"{num} and {num2} are Twin Prime")
else:
    print(f"{num} and {num2} are Not Twin Prime")