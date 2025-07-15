#Spy no.
def factor(n):
    li=[]
    for i in range(1,n):
        if n%i==0:
            li.append(i)
    return li
n=int(input("Enter the no. = "))
s=0
p=1
for i in factor(n):
    s+=i
    p*=i
if s==p:
    print("Spy No.")
else:
    print("Not Spy No.")