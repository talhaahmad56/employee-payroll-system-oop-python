class Employee:
    def __init__(self, emp_id , name , base_salary):
        self.emp_id = emp_id
        self.name = name
        self.base_salary = base_salary

    def calculate_salary(self):
        return self.base_salary
    
    def __str__(self):
        return f"Employee ID : {self.emp_id} | Employee name : {self.name}"
    

class Manager (Employee):
    def __init__(self , emp_id , name , base_salary , bonus):
        super().__init__(emp_id , name , base_salary)
        self.bonus = bonus

    def calculate_salary(self):
        return super().calculate_salary() + self.bonus
    
class Developer (Employee):
    def __init__(self , emp_id , name , base_salary , overtime_hours):
        super().__init__(emp_id , name , base_salary)
        self.overtime_hours = overtime_hours

    def calculate_salary(self):
        return super().calculate_salary() + (self.overtime_hours * 5000)
    

def get_positive_int(message):
    while True:
        try:
            value = int(input(message))
            if value > 0:
                return value
            print("Value must be greater than 0.")
        except ValueError:
            print("Please enter a valid number.")


def get_non_negative_int(message):
    while True:
        try:
            value = int(input(message))
            if value >= 0:
                return value
            print("Value cannot be negative.")
        except ValueError:
            print("Please enter a valid number.")


def is_unique_id(emp_id, employees):
    for emp in employees:
        if emp.emp_id == emp_id:
            return False
    return True


employees = []

while True:
    print("\n1. Add Manager")
    print("2. Add Developer")
    print("3. Show All Salaries")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        while True:
            emp_id = get_positive_int("Enter Employee ID: ")
            if is_unique_id(emp_id, employees):
                break
            print("Employee ID already exists. Try another.")

        name = input("Enter Name: ")
        base_salary = get_positive_int("Enter Base Salary: ")
        bonus = get_non_negative_int("Enter Bonus: ")

        manager = Manager(emp_id, name, base_salary, bonus)
        employees.append(manager)
        print("Manager added successfully!")

    elif choice == "2":
        while True:
            emp_id = get_positive_int("Enter Employee ID: ")
            if is_unique_id(emp_id, employees):
                break
            print("Employee ID already exists. Try another.")

        name = input("Enter Name: ")
        base_salary = get_positive_int("Enter Base Salary: ")
        overtime = get_non_negative_int("Enter Overtime Hours: ")

        developer = Developer(emp_id, name, base_salary, overtime)
        employees.append(developer)
        print("Developer added successfully!")

    elif choice == "3":
        if not employees:
            print("No employees added yet.")
        else:
            for emp in employees:
                print(emp)
                print("Total Salary:", emp.calculate_salary())
                print("-" * 30)

    elif choice == "4":
        print("Exiting program...")
        break

    else:
        print("Invalid choice. Try again.")