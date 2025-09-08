# ✅ Creating a list of heroes (list of strings)
hero = ["ben", "spider man", "iron man"]

# ✅ Creating a list of marks (list of numbers)
marks = [10.5, 85.1, 4, 2, 900]

# ✅ Printing the lists
print(hero)       # Output: ['ben', 'spider man', 'iron man']
print(marks)      # Output: [10.5, 85.1, 4, 2, 900]

# ✅ A list can store different datatypes together (int, float, string, char, boolean)
datatypes = [10, 15.2, "chandan", 'r', True]
print(datatypes)  # Output: [10, 15.2, 'chandan', 'r', True]

# ✅ type() function shows the datatype of a variable
print(type(hero))       # <class 'list'>
print(type(marks))      # <class 'list'>
print(type(datatypes))  # <class 'list'>

# ✅ Lists are mutable → we can modify elements using index
hero[0] = "hulk"        # Replaces "ben" with "hulk"
print(hero)             # Output: ['hulk', 'spider man', 'iron man']
