"""
create student class that takes name & marks
of 3 subjects as arguments in constructor. Then
create a method to print the average
"""

class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
        print("-------------------------------------")

    # method
    def average(self):
        avg = 0
        for mark in self.marks:
            avg = avg + mark
        print("Hi,", self.name, "Your average score is: ", avg)

s1 = Student("Hira", [90, 98, 95])
s1.average()

s2 = Student("Himel", [10, 20, 30])
s2.average()
