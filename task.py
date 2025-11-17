class Diary():
    def __init__(self):
        self.students = []
    
    def add_student(self, name: str, grade: double):
        for i in enumerate(self.students):
            if student[0] == name:
                self.student(i) == (name, grade)
                return self.students.append((name, grade))

    def get_grade(self name:str, name: double):
        for student in self.students:
            if student[0] == name:
                return student[1]
        return None

    
def avg_grade(self.students):
    return sum(self.students) / len(self.students)
