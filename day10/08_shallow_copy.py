a = [[1, 2], [3, 4]]
b = a.copy()  # This creates a shallow copy of the list 'a'

print(a is b)  # Output: False (a and b are different objects)
print(a[0] is b[0])  # Output: True (the inner lists are the same objects)
print(a == b)  # Output: True (the contents of the lists are the same)

a[0].append(99)  # Modifying the inner list of 'a'
print(a)  # Output: [[1, 2, 99], [3, 4]]
print(b)
# Output: [[1, 2, 99], [3, 4]] (the change is reflected in 'b' because it shares the same inner list)

a.append([5, 6])  # Modifying the outer list of 'a'
print(a)  # Output: [[1, 2, 99], [3, 4], [5, 6]]
print(b)
# Output: [[1, 2, 99], [3, 4]] (the change is not reflected in 'b' because it is a shallow copy and does not include the new inner list)
