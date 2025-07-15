#map() sq. of list element
numbers_list = [2, 4, 5, 1, 3, 7, 8, 9, 10]      
numbers_list = list(map( lambda num: num ** 2 , numbers_list))      
print( 'Square of each number in the given list:',numbers_list)