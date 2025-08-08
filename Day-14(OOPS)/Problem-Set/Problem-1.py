# 1. Create a class Person, and extend it with Employee and Manager classes.

class Person:
    
    def __init__(self,name,age):
        self.name = name
        self.age = age
        
    def __str__(self):
        return f'Name : {self.name}, Age : {self.age}'
    
class Employee(Person):
    
    def __init__(self,name,age,employee_id,department):
        super().__init__(name,age)
        self.employee_id = employee_id
        self.department  = department 
        
    def __str__(self):
        return f'Employee id : {self.employee_id}\nName : {self.name}\nAge : {self.age}\nDepartment : {self.department}'
    
class Manager(Employee):
    
    def __init__(self,name,age,employee_id,department,team_size, level):
        super().__init__(name, age, employee_id, department)
        self.team_size = team_size
        self.level     = level
        
    def __str__(self):
        return f'Employee id : {self.employee_id}\nName : {self.name}\nAge : {self.age}\nDepartment : {self.department}\nTeam size : {self.team_size}\nLevel : {self.level}'