from utils import cube

print(cube(5))
# Output: 125


# Writing to a file
def write_to_file(filename, content):
    with open(filename, "w") as file:
        file.write(content)


write_to_file(
    "day6/sample.txt", "Name: Tridib\nCompany: ABC\nFavourite Language: Python"
)


# Reading from the file
def read_from_file(filename):
    with open(filename, "r") as file:
        return file.read()


content = read_from_file("day6/sample.txt")
print(content)

# Output: Name: Tridib
#         Company: ABC
#         Favourite Language: Python
