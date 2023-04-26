class Student:  # defining what a stdent is within the confines of our program
    def __init__(self, name, major, gpa, is_on_probation):  # initialize function
        self.name = name
        self.major = major  # self. whatever is = to whater is being passed into it
        self.gpa = gpa
        self.is_on_probation = is_on_probation

    def take_test(self):
        print("The student takes a test")

    def go_to_school(self):
        print("The student goes to school")

    def eats_lunch(self):
        print("The student eats lunch")

    def on_honor_roll(self):
        if self.gpa >= 3.5:
            return True
        else:
            return False

        # and object is an instance of a clas....
        # see "actual_Student



