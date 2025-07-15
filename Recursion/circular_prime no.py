def prime(n,i):
    if  n%i==0:
      if n!=i:
        return False
    else:
        return prime(n,i+1)   
    return True
def cir(a):
    s=str(a)
    a=int(s[1:]+s[0])
    return a
a=int(input("Enter No.:"))
print(a)
if prime(a,i=2):
   x=cir(a)
   print(x)
   if a!=x:
      prime(x,i=2) 
   print("Circular Prime")
else:
  print("Not Circular Prime No")