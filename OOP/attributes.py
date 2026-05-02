"""
There are two types of attributes
1) Class Attributes (common like college name for same college student)
2) Object Attributes (student name all names are diffrent)
"""

# creating class
class Student:
    college_name = "Demra Ideal College" # class attributes
    # parameteirzed constructor 
    def __init__(self, fullname, marks):  
        self.name = fullname # object attributes
        self.marks = marks # object attributes
        print("-------------------------------------")
        print("adding new student in Database...")

# creating object
s1 = Student("hira", 100)
print(s1.name)
print(s1.marks)
print(s1.college_name)

s2 = Student("himel", 88)
print(s2.name)
print(s2.marks)
print(s2.college_name)
