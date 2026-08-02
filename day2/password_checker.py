password = input("Enter your password: ")

# Check password length
if len(password) < 8:
    print("Password is Weak")
else:
    print("Password is Strong")
