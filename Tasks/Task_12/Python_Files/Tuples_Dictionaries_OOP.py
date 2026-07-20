class Employee:
    def __init__(self, emp_id, name, department, salary):
        self.emp_id = emp_id
        self.name = name
        # details Is A Tuple Containing Department & Salary
        self.details = (department, salary)
 
    def show_details(self):
        department, salary = self.details
        print(f"Employee ID: {self.emp_id}")
        print(f"Name: {self.name}")
        print(f"Department: {department}")
        print(f"Salary: {salary}")
 
 
def main():
    # Dictionary: employee ID (Key) -> Employee Object (Value)
    employees = {}
 
    # Add 3 employees
    employees["E101"] = Employee("E101", "Mihir Patil", "Engineering", 75000)
    employees["E102"] = Employee("E102", "Kunal Yendole", "Marketing", 62000)
    employees["E103"] = Employee("E103", "Shubham Chavan", "Finance", 68000)
 
    # Display All Employees Using A Loop
    print("All Employee Records:\n")
    for emp_id, employee in employees.items():
        employee.show_details()
 
 
if __name__ == "__main__":
    main()
 