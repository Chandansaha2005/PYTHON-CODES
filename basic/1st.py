#WAP to calc. the gcd of two given no.
a=int(input("Enter the first no. = "))
b=int(input("Enter the second no. = "))
p=1
i=2
x=a
y=b
while(i<=a and i<=b):
  if(a%i==0 and b%i==0):
    p*=i
    a//=i
    b//=i
  else:
    i+=1
print("The gcd of",x,"and",y,"is",p)