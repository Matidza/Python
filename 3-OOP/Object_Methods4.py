# Create a Class
class Person:
    # Create a constructor function
    def __init__(self, name, surname, age, country):
        self.name = name
        self.surname = surname
        self.age = age
        self.country = country

    # Create Object Method
    def person_info(self):
        return f"Hi, i'm {self.name} {self.surname} and i'm {self.age} years old and im from {self.country}"
    
# Create class Object
p = Person("Zwivhuya", "Mukwevho", 25, "South Africa")
print(p.person_info())