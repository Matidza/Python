# Creating a class

class Person:
    pass

# Creating an object
p = Person()
print(p)

"""
class constructor function
"""

class Person:
    # create class constructor
    def __init__(self, name, surname):
        self.name, self.surname = name, surname

# create an object
p = Person("Zwivhuya", "mukwevho")
print(p)
#print(p.person) # Object Method

"""
Object Method
"""
class Person:
    def __init__(self, name, surname, age):
        self.name = name
        self.surname = surname
        self.age = age

    # Class Obeject method
    def person_info(self):
        return f'My name is {self.name} {self.surname} and i am {self.age}.'
p = Person("Zwivhuya", "Mukwevho", 26)
print(p)
print(p.person_info())