# creating class
class Student:
    # default constructor
    def __init__(self):
        pass

    # parameteirzed constructor 
    def __init__(self, fullname, marks):  
        self.name = fullname
        self.marks = marks
        print("adding new student in Database..")

# creating object
s1 = Student("hira", 100)
print(s1.name)
print(s1.marks)

s2 = Student("himel", 88)
print(s2.name)
print(s2.marks)
