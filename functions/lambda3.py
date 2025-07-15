#lambda
add = lambda x, y: x + y
result = add(3, 5)
print(result)

students = [('Anusha', 22), ('Tanbi', 18), ('Sanchayan', 21)]
students.sort(key=lambda student: student[1])  # Sort by Name
print(students) 

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)  # [2, 4, 6, 8, 10]

numbers = [1, 2, 3, 4, 5]
numbers = list(map(lambda x: x**2, numbers))
print(numbers) 

is_positive = lambda x: True if (x > 0) else False
print(is_positive(5))
print(is_positive(-3))  


from functools import reduce
product = reduce(lambda x, y: x * y, [1, 2, 3, 4,5])
print(product)  # 24 (1*2*3*4)