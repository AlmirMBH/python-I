class Student:

    def __init__(self, name, last_name, major, gpa, is_on_probation):
        self.name = name
        self.last_name = last_name
        self.major = major
        self.gpa = gpa
        self.is_on_probation = is_on_probation

    def on_honor_roll(self):
        if self.gpa >= 3.5:
            return True
        else:
            return False


