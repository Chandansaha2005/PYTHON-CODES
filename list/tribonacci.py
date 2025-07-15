#WAP to print tribonacci series: 1 1 1 3 5 9 17 31 57 ... n
li=[]
a=1
b=1
c=1
s=0
n=int(input("Enter the Range = "))
li.append(a)
li.append(b)
li.append(c)
for i in range(4,n+1,1):
    s=a+b+c
    li.append(s)
    a=b
    b=c
    c=s
print(li)