import copy

a = [[1, 2], [3, 4]]
b = copy.deepcopy(a)  # This creates a deep copy of the list 'a'

print(a is b)  # Output: False (a and b are different objects)
print(a[0] is b[0])  # Output: False (the inner lists are also different objects)
print(a == b)  # Output: True (the contents of the lists are the same)

a[0].append(99)  # Modifying the inner list of 'a'
print(a)  # Output: [[1, 2, 99], [3, 4]]
print(b)
# Output: [[1, 2], [3, 4]] (the change is not reflected in 'b' because it is a deep copy and does not share the same inner list)

c = copy.copy(a)  # This creates a shallow copy of the list 'a'
print(a is c)  # Output: False (a and c are different objects)
print(a[0] is c[0])  # Output: True (the inner lists are the same objects)
print(a == c)  # Output: True (the contents of the lists are the same)

a[0].append(100)  # Modifying the inner list of 'a'
print(a)  # Output: [[1, 2, 99, 100], [3, 4]]
print(c)
# Output: [[1, 2, 99, 100], [3, 4]] (the change is reflected in 'c' because it is a shallow copy and shares the same inner list)
