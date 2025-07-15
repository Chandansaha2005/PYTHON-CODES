#WAP to create a list of numbers in the range 1 to 10.Then delete all the even numbers from the list and print the final list.
li=list(range(1,11))
print("LIST :",li)
print("Odd List :",list(filter(lambda x:x%2==0,li)))
'''
for i in range(10):
    if li[i]%2==1:
        li[i]=' '
print(li)
'''