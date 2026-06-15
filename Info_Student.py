class Student:
    def __init__(self):
        self.name = "rama"
        self.age = "23"
        self.quali = "BE"
        self.address = "Bangalore"
        
    def eat(self):
        print("stduent is eating" )
        
    def study(self):
        print("student is studying")
    
S1=Student()
print (S1.name)
print (S1.age)
print (S1.quali)
print (S1.address)
S1.eat()
S1.study()    
