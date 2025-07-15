#WAP to enter a number and then calculate the sum of its digits using while loop
s=0
n=int(input("Enter the no. = "))
x=n
while n!=0:
    s+=n%10
    n//=10
print("Sum of digit : ",s)