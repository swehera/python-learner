"""
------------Abstraction------------
Hiding the implementation details of a class and only
showing the essential features to the user 
"""
class Car:
    def __init__(self):
        self.acc = False
        self.brk = False
        self.clutch = False
    
    def start(self):
        self.acc = True
        self.clutch = True
        print("car started..")
    
    def stop(self):
        self.acc = False
        self.clutch = False
        self.br = False
        print("car stoped..")
    
    def slow_car(self):
        self.brk = True
        print("car break for slow")


c1 = Car()
c1.start()
c1.slow_car()
c1.stop()