# Saves student information to a file
def save_student(name, age, company):
    with open("day6/students.txt", "a") as file:
        file.write(f"{name},{age},{company}\n")


save_student("Tridib", 25, "ABC")
save_student("Rahul", 28, "TCS")


# Displays student information from the file
def show_students():
    print(f"{'-' * 20}\nStudent Information\n{'-' * 20}\n")
    with open("day6/students.txt", "r") as file:
        for line in file:
            info = line.split(",")
            if len(info) == 3:
                print(
                    f"Name : {info[0]}\nAge : {info[1]}\nCompany : {info[2]}{'-' * 20}"
                )


show_students()
