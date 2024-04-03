class Teacher():
    def __init__(self, name):
        self.name = name
    def teach(self):
        print(f"учитель {self.name} учит")

class School():
    def __init__(self, new_teacher):
        self.teacher = new_teacher
    #def start_lesson():
     #   teacher.teach()

my_teacher = Teacher("John")
my_teacher.teach()

new_school = School(my_teacher)
#new_school.start_lesson()

#name = School(my_teacher)
#def __init__(self, new_teacher):
#    self.teacher = new_teacher





