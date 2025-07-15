#WAP to demonstrate the list slice operation 
li=[]
n=int(input("Enter the Range = "))
for i in range(0,n):
    li.append(int(input("Enter the no. = ")))
'''
 Syntax of slice()
 
 variable = slice(start,end,step)
 
'''
x=slice(0,n,1)
print(li[x])