### 2. Converting a List of Strings to Uppercase

names = ["Ishita", "Anish", "Sanchayan"]
names = list(map(str.upper, names))
print(names)  


### 3. Applying a Custom Function to Each Element


# Custom function to format strings
def format_name(name):
    return name.title()

names = ["animesh pramanick", "piyosee pramanick", "shreya pramanik"]
formatted_names = list(map(format_name, names))
print(formatted_names)  


### 4. Using map() with Multiple Iterables

# Adding corresponding elements of two lists
list1 = [1, 2, 3, 4]
list2 = [5, 6, 7, 8]
sum_list = list(map(lambda x, y: x + y, list1, list2))
print(sum_list)  


### 5. Applying map() to Strings

# Mapping ord() function to a string
word = "piyomesh"
ascii_values = list(map(ord, word))
print(ascii_values)  # Output: [104, 101, 108, 108, 111]


### 6. Combining map() with filter()


# Filtering and mapping simultaneously
numbers = [1, 2, 3, 4, 5, 6]
filtered_doubled = list(map(lambda x: x * 2, filter(lambda x: x % 2 == 0, numbers)))
print(filtered_doubled)  # Output: [4, 8, 12]