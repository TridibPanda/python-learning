fruits = ["Apple", "Banana", "Mango"]

print(fruits.index("Mango"))  # Item index
# Output: 2
print(fruits.count("Mango"))  # Counts total occurrences.
# Output: 1

# Add item in list
fruits.append("Orange")
print(fruits)
# Output: ['Apple', 'Banana', 'Mango', 'Orange']

# Insert item in list
fruits.insert(1, "Grapes")
print(fruits)
# Output: ['Apple', 'Grapes', 'Banana', 'Mango', 'Orange']

# Remove item from list
fruits.remove("Banana")
print(fruits)
# Output: ['Apple', 'Grapes', 'Mango', 'Orange']

# Reverse the list in-place
fruits.reverse()
print(fruits)
# Output: ['Orange', 'Mango', 'Grapes', 'Apple']

# Copy from list
copy_fruits = fruits.copy()
print(copy_fruits)
# Output: ['Orange', 'Mango', 'Grapes', 'Apple']

# Extend the list
more_fruits = ["Cherry", "Banana"]
fruits.extend(more_fruits)
print(fruits)
# Output: ['Orange', 'Mango', 'Grapes', 'Apple', 'Cherry', 'Banana']

# Removes last item
fruits.pop()
print(fruits)
# Output: ['Orange', 'Mango', 'Grapes', 'Apple', 'Cherry']

# Sort the list in ascending order
fruits.sort()
print(fruits)
# Output: ['Apple', 'Cherry', 'Grapes', 'Mango', 'Orange']

# Remove all items from list
fruits.clear()
print(fruits)
# Output: []
