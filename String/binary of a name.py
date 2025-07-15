#WAP to convert a name into its binnary equivalent
n=input("Enter the string : ")
for i in n:
    s=''
    d=ord(i)
    print(i," = ",d,end=" = ")
    while (d!=0):
        r=d%2
        s+=str(r)
        d//=2
    #print(s)
    b=s[::-1]
    print(b)