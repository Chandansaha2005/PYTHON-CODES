#WAP that creates a list of numbers from 1-20 that are either divisible by 2 or divisible by 4 without using the filter function
li=list(range(1,(int(input("Enter the range :")))+1))
new_list=list(filter(lambda x: x%2==0 or x%4==0,li))
print("List = ",li)
print("New list = ",new_list)