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
    
    # static method
    @staticmethod # decorator 
    def hello():
        print("Hello, I am static method")

s1 = Student("Hira", [90, 98, 95])
s1.average()
s1.hello()

s2 = Student("Himel", [10, 20, 30])
s2.average()
s2.hello()

