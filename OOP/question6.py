#method overriding
class Employee:
    def __init__(self,name):
        self.name = name

    def calculate_salary(self):
        return "This method calculates salary"

class Manager(Employee):
     def __init__(self,name,salary):
         super().__init__(name)
         self.salary = salary

     def calculate_salary(self):
         return f"{self.name}'s salary is {self.salary}"


emp1 = Employee("Habiba")
print(emp1.calculate_salary())
emp2 = Manager("Habiba",20000)
print(emp2.calculate_salary())
