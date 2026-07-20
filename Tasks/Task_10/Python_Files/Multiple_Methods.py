class Employee:
    def __init__(self, name, salary):
        self.name   = name
        self.salary = salary
 
    def display_details(self):
        print("Employee:", self.name)
        print("Salary: Rs.",self.salary)
 
    def give_raise(self, amount):
        self.salary += amount
        print("Raise Of Rs.", amount, "Applied! New Salary: Rs.", self.salary)
 
    def yearly_bonus(self):
        bonus = self.salary * 0.10
        print("Yearly Bonus For", self.name, ": Rs.", bonus)

emp = Employee("Mihir", 50000)
emp.display_details()
emp.give_raise(5000)
emp.yearly_bonus()