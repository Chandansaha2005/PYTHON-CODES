#Write a python program creates a list of 10 random integers.then create two lists—Odd list and Even list that has all odd and even values in the list respectively
li,n=[],int(input("Enter the range : "))
for i in range(n):
    li.append(int(input("Enter the no. = ")))
odd=list(filter(lambda x : x%2!=0,li))
even=list(filter(lambda x : x not in odd and x!=0,li))
print("Odd List : ",odd)
print("Even List : ",even)