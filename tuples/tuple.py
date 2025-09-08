# ✅ Creating a tuple (ordered, immutable collection)
tuple = (2, 8, 5, 6, 7)

# ✅ Accessing elements by index
print(tuple[0])  # 2 (first element)
print(tuple[4])  # 7 (fifth element)

# ❌ Out of range index gives error
# print(tuple[5])  # Error: IndexError

# ❌ Tuples are immutable → cannot modify elements
# tuple[0] = 9  
# print(tuple)  # Error: 'tuple' object does not support item assignment

# ✅ Creating an empty tuple
empty_tup = ()
print(empty_tup)        # ()
print(type(empty_tup))  # <class 'tuple'>

# ❌ Be careful with single element tuple
# Without comma, Python treats it as int
# single_valued_tuple = (1)  # this is just int, NOT tuple

# ✅ Correct way to create a single element tuple → add a comma
single_valued_tuple = (1,)
print(single_valued_tuple)  # (1,)
print(type(single_valued_tuple))  # <class 'tuple'>

# 📝 Short Notes (Tuple)

# Tuple: Ordered, immutable collection in Python → defined with ().
# Indexing: Works same as list (tuple[0], tuple[1] …).
# Immutability: Cannot add, remove, or change elements.
# Empty tuple: empty_tup = ().
# Single element tuple: Must use a comma → (1,).