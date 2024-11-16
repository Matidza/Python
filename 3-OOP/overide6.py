from modify5 import Person


class Student(Person):
    def __init__(self, name, gender):
        self.gender = gender 
        super().__init__(name)

    def person_info(self):
        gender = "He" if self.gender == "male" else "She"
        return f"My name is {self.name} and im a {self.gender}"

s1 = Person("Zwivhuya", "male")
print(s1.person_info())