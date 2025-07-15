#WAP to create a list of numbers in the specified range in particular steps. Reverse the list and print its values
n=int(input("Enter the range ="))
li=list(range(1,n+1))
print("List :",li)
print("Reverse List :",li[::-1])