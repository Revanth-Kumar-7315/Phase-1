# 3. Create a Student class and then derive a GraduateStudent from it using inheritance. Add super().
class Student:
    
    def __init__(self,name,roll_no):
        self.name    = name
        self.roll_no = roll_no
        
class GraduateStudent(Student):
    
    def __init__(self,name,roll_no,thesis_title):
        super().__init__(name,roll_no)
        self.thesis_title = thesis_title