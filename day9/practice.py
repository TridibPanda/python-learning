class Employee:
    def __init__(self, name, company, salary):
        self.name = name
        self.company = company
        self.salary = salary


employee1 = Employee("Tridib", "ABC", 1200000)
employee2 = Employee("Rahul", "TCS", 1500000)
employee3 = Employee("Rohit", "CDE", 800000)

print(
    f"Name: {employee1.name}, Company: {employee1.company}, Salary: {employee1.salary}"
)
print(
    f"Name: {employee2.name}, Company: {employee2.company}, Salary: {employee2.salary}"
)
print(
    f"Name: {employee3.name}, Company: {employee3.company}, Salary: {employee3.salary}"
)
# Output:
# Name: Tridib, Company: ABC, Salary: 1200000
# Name: Rahul, Company: TCS, Salary: 1500000
# Name: Rohit, Company: CDE, Salary: 800000
