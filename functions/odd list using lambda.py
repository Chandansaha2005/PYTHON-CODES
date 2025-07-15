#lambda
list1 = [35, 12, 69, 55, 75, 14, 73]      
odd_list = list(filter( lambda num: num % 2 != 0, list1))
print('The list of odd number is:',odd_list) 