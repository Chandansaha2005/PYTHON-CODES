#WAP o create a list of numbers divisible by 2 or 4 using filter() function
n = int ( input("Enter the range = "))
#li=list(range(1,n+1))
li2=list(filter(lambda x:x%2==0 or x%4==0,list(range(1,n+1))))
print(li2)
