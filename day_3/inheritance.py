class Person:
    def __init__(self, name, occupation):
        self.name = name
        self.occupation = occupation

    def return_occupation(self):
        return self.occupation


class Teacher(Person):
    def __init__(self, name, occupation, subject):
        super().__init__(name, occupation)  #Oh shit, it's a superclass!
        self.subject = subject

    def return_teacher_subject(self):
        return self.subject

    def find_teacher(self, name):
        for name in self:
            if name == self.name:
                self.return_occupation()
                self.return_teacher_subject


    