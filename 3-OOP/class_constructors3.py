# Create a Class
class Person:
    # Create/Use a Constructor
    def __init__(self, name):
        # slef allows to attach parametors to the class
        self.name = name

# Create an object
p = Person("Zwivhuya")
print(p) # this print the Class object
print(p.name) # This passes the argument passed through the Class

"""
Lets Add More Parametors to the Constructor Function
"""

# Create a Class
class PersonInfo:
    # Create/Use a Constructor
    def __init__(self, name, surname, age, country, city):
        # slef allows to attach parametors to the class
        self.name = name
        self.surname = surname
        self.age = age
        self.country = country
        self.city = city

# Create an object
id = PersonInfo("Zwivhuya", "Mukwevho", "26", "South Africa", "JHB")
print(id)
print(type(id))
print(id.surname)
print(id.age)
print(f"I'm from the country of {id.country}", sep=" ")

"""
More Parametors to the Constructor
"""
