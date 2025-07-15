#HAPPY no.
import math
def num_square_sum(n):#n=10
    square_sum = 0  
    while n != 0:#0!=0
        square_sum =square_sum+ (n % 10) ** 2 #1
        n =n// 10#n=0
    return square_sum#1
def is_happy_number(n):
    slow = fast = n   #slow==49 fast=49
    while True:
        slow = num_square_sum(slow)#130
        fast = num_square_sum(num_square_sum(fast))
        if slow == fast:#1==1
            break
    return slow == 1 
n = int(input("Enter the No. = "))
if is_happy_number(n):#n=49
    print(n," is a Happy number")
else:
    print(n," is not a Happy number")