#How can we utilize the objects created from the class blueprint employee , to get the company's total payroll in class Payroll ?
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

class Payroll:
    def __init__(self, employees):
        #list of employee objects
        self.employees = employees

    def total_payroll(self):
        total = sum(employee.salary for employee in self.employees)
        return total

emp1 = Employee("Bob", 2000)
emp2 = Employee("Jack", 5000)
emp3 = Employee("Jacky", 6000)

employees = [emp1, emp2, emp3]
payroll = Payroll(employees)
total = payroll.total_payroll()
print(f"total payroll:{total}")

