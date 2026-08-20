# Same function, different object types
print(len("Tridib"))  # Output: 6
print(len([10, 20, 30, 40]))  # Output: 4
print(len((1, 2, 3)))  # Output: 3
print(max(10, 20))  # Output: 20
print(max("10", "20"))  # Output: 20

# Same operator, different behavior
print(10 + 20)  # Output: 30
print("Hello " + "Bro")  # Output: Hello Bro
print([1, 2] + [3, 4])  # Output: [1, 2, 3, 4]
print("Hi" * 3)  # Output: HiHiHi
print(3 * 3)  # Output: 9
