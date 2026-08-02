age = int(input("Age: "))
has_license = input("License (yes/no): ")

# Nested if statement
if age >= 18:
    if has_license.lower() == "yes":
        print("You can drive.")
    else:
        print("Get a driving license first.")
else:
    print("You are underage.")
