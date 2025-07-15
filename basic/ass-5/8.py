#WAP to disply leap year from a range of years
m=int(input("Enter the starting year = "))
n=int(input("Enter the ending year = "))
f=1
for i in range(m,n+1):
    if (i%4==0 or i%400==0) and i%100!=0 :
        print(i,end=" ")
    