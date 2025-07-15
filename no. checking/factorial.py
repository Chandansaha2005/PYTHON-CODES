#Factorial of a no.
n=int(input("Enetr the no = "))
li=list(range(1,n+1))
f=1
for i in li:
   f*=i 
print("Facotial of ",n,"is",f)