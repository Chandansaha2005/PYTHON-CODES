# ✅ Creating a sample list
numbers = [10, 20, 30, 40, 20]
chars = ["b", "d", "a", "c"]

# 1. append(x) → Adds an element at the end
numbers.append(50)
print(numbers)  # [10, 20, 30, 40, 20, 50]

# 2. insert(i, x) → Inserts element at a given index
numbers.insert(2, 99)
print(numbers)  # [10, 20, 99, 30, 40, 20, 50]

# 3. remove(x) → Removes first occurrence of given value
numbers.remove(20)
print(numbers)  # [10, 99, 30, 40, 20, 50]

# 4. pop([i]) → Removes element at given index (default: last)
numbers.pop()
print(numbers)  # [10, 99, 30, 40, 20]

# 5. clear() → Removes all elements
temp = [1, 2, 3]
temp.clear()
print(temp)  # []

# 6. index(x) → Returns index of first occurrence
print(numbers.index(30))  # 2

# 7. count(x) → Counts occurrences of element
print(numbers.count(20))  # 1

# 8. sort() → Sorts list in ascending order
chars.sort()
print(chars)  # ['a', 'b', 'c', 'd']

# 9. sort(reverse=True) → Sorts list in descending order
chars.sort(reverse=True)
print(chars)  # ['d', 'c', 'b', 'a']

# 10. reverse() → Reverses the list
chars.reverse()
print(chars)  # ['a', 'b', 'c', 'd'] (back to original order)

# 11. copy() → Returns a shallow copy
new_list = numbers.copy()
print(new_list)  # [10, 99, 30, 40, 20]

# 12. extend(iterable) → Adds elements of another iterable
numbers.extend([60, 70])
print(numbers)  # [10, 99, 30, 40, 20, 60, 70]

# 13. len(list) → Returns length of list
print(len(numbers))  # 7

# 14. max(list) → Returns maximum element
print(max(numbers))  # 99

# 15. min(list) → Returns minimum element
print(min(numbers))  # 10

# 16. sum(list) → Returns sum of numeric elements
print(sum(numbers))  # 329

# 17. any(list) → True if at least one element is True
print(any([0, False, 5]))  # True

# 18. all(list) → True if all elements are True
print(all([1, True, 3]))   # True
print(all([1, 0, 3]))      # False

# 19. slicing → Accessing parts of list
print(numbers[1:4])   # [99, 30, 40]  (index 1 to 3)
print(numbers[::-1])  # reverse using slicing

# 20. nested lists → List inside a list
nested = [[1, 2], [3, 4], [5, 6]]
print(nested[1][0])  # 3 (row 2, col 1)

# 🔑 Quick Summary (For Fast Revision)

# Add/Insert: append(), insert(), extend()
# Remove: remove(), pop(), clear()
# Info: index(), count(), len(), max(), min(), sum()
# Sorting/Ordering: sort(), reverse()
# Copying: copy()
# Logic: any(), all()
# Accessing: Indexing, Slicing, Nested lists