# Create a Class
class Person:
    # class constructor
    def __init__(self, name="Zwivhuya", surname="Mukwevho", age=26, skills=[]):
        self.name = name
        self.surname = surname 
        self.age = age 
        self.skills = []

    # Object method
    def person_info(self):
        return f"{self.name} {self.surname}"
    #
    def add_skills(self, skills):
        self.skills.append(skills)
p = Person()
print(p.person_info())

p.add_skills("Pyhton")
p.add_skills("Django")
p.add_skills("Flask")
p.add_skills("HTML, CSS")
print(p.skills)

p2 = Person()
print(p2.skills)