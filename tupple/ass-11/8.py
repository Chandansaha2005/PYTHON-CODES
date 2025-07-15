#WAP to print the name of the topper and her marks in 4 subjects wherein the marks are specified as a list in the tuple Topper
li,sum,m,j,sub=[],[],0,0,['math','physics','chemistry','comp. sci.']
n=int(input("Enter the no. of students : "))
for i in range(n):
    topper,marks,s=(),[],0
    topper += (input("Enter the student name :").title(),)
    for i in range(4):
        x=int(input(f"Enter the Marks of {sub[i]} :"))
        marks.append(x)
        s+=x
    sum.append(s)
    topper +=(marks,)
    li.append(topper)
    
print((li))
for i in range(n):
    if sum[i]>m:
        m,j=sum[i],i
print("Name of the topper :",li[j][0],"\nMarks of the topper :",li[j][1])