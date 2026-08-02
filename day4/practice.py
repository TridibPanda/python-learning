technologies = ["React Native", "Flutter", "Python", "FastAPI", "OpenAI"]

for index, item in enumerate(technologies, start=1):
    print(f"{index}. {item}")

# Output:
# 1. React Native
# 2. Flutter
# 3. Python
# 4. FastAPI
# 5. OpenAI

user_input = input("Enter one more technology: ")

technologies.append(user_input)
# Output : If user input is "JavaScript" then updated list:  ['React Native', 'Flutter', 'Python', 'FastAPI', 'OpenAI', 'JavaScript']
print(technologies)
for index, item in enumerate(technologies, start=1):
    print(f"{index}. {item}")

# Output: If user input is "JavaScript" then updated list:
# 1. React Native
# 2. Flutter
# 3. Python
# 4. FastAPI
# 5. OpenAI
# 6. JavaScript
