from classes_objects import Student


class asianStudent(Student):

    def take_test(self):
        print("The student takes a test")

    def go_to_school(self):
        print("The student goes to school")

    def eats_lunch(self):
        print("The student eats bento")  # overrides original lunch

    def eats_boogers(self):     # new to asian student
        print("The student picks his nose")
