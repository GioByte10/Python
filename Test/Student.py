class Student:

    def __init__(self, name, gpa, school, passed):
        self.name = name
        self.gpa = gpa
        self.school = school
        self.passed = passed

    def __str__(self):
        return self.name + '\n' + str(self.gpa)