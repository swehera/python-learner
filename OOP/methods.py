# creating class
class Student:
    college_name = "Demra Ideal College" # class attributes
    # parameteirzed constructor 
    def __init__(self, fullname, marks):  
        self.name = fullname # object attributes
        self.marks = marks # object attributes
        print("-------------------------------------")
        print("adding new student in Database...")
    
    # methods
    def welcome(self):
        print("Welcome students", self.name)
    
    # methods
    def get_marks(self):
        return self.marks
    


# creating object
s1 = Student("hira", 100)
print(s1.name)
print(s1.marks)
print(s1.college_name)
s1.welcome()
print(s1.get_marks())

s2 = Student("himel", 88)
print(s2.name)
print(s2.marks)
print(s2.college_name)
s2.welcome()
print(s2.get_marks())

