import csv

class Employee:
    def __init__(self,  name: str, surname: str, age: int, salary: int):
        self.name = name
        self.surname = surname
        self.age = age
        self.salary = salary

    def print_info(self):
        print(f"Employee name: {self.name} {self.surname}\nSalary: {self.salary}\nAge: {self.age}")

with open("dataset1.csv", 'r') as csv_file:
    csv_reader = csv.reader(csv_file)
    next(csv_reader)
    employee_list = [Employee(line[0], line[1], line[2], line[3]) for line in csv_reader]

print("Employee with the least salary:")
min(employee_list, key=lambda emp: emp.salary).print_info()
print()
print("The oldest employee:")
max(employee_list, key=lambda emp: emp.age).print_info()
