#WAP to convert a name into its binnary equivalent
li= list(range(ord('A'),ord('Z')+1)) + list(range(ord('a'),ord('z')+1))
print(li)
for i in li:
    s=''
    d=i
    print(chr(i)," = ",d,end=" = ")
    while (d!=0):
        r=d%2
        s+=str(r)
        d//=2
    #print(s)
    b=s[::-1]
    print(b)