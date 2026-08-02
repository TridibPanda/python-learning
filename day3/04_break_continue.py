for i in range(10):
    if i == 5:
        break  # Exit the loop when i is equal to 5
    print(i)
# Output: 0, 1, 2, 3, 4

for i in range(5):
    if i == 2:
        continue  # Skip the rest of the loop when i is equal to 2
    print(i)
# Output: 0, 1, 3, 4

count = 1
while count <= 10:
    if count == 5:
        count += 1
        break  # Exit the loop when count is equal to 5
    print(count)
    count += 1
# Output: 1, 2, 3, 4

increment = 1
while increment <= 5:
    if increment == 2:
        increment += 1
        continue  # Skip the rest of the loop when increment is equal to 2
    print(increment)
    increment += 1
# Output: 1, 3, 4, 5
