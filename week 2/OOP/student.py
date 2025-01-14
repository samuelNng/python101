class Student:
    def __init__(self, name, age, grade,height):
        self.name = name
        self.age = age
        self.grade = grade
        self.height= height
    #for str output
    def __str__(self):
        return f"{self.name}, Age:{self.age},Grade:{self.grade}, Height: {self.height}"


        
        
# Creating an instance of Student
new_student = Student("Alice", 20, "A", 165)
old_student = Student('Dan' ,18, 'A' ,164)


print(new_student)
