my_student = {
    "name": "Rolf Smith",
    "grades": [70,88,90,91]
}

def average_grade(student):
    return sum(student["grades"]) / len(student["grades"])

# average_grade(my_student)
# print(average_grade(my_student))

class Student:
    def __init__(self,new_name,new_grades):
        self.name = new_name
        self.grades = new_grades

    def average(self):
        return sum(self.grades) / len(self.grades)

student_one = Student("Rolf Smith",[70,88,90,91])
print(student_one)


