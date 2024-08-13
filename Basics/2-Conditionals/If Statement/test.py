# Tupple

name_list = ('Zwivhuya', 'Michele', 'Wanga', 'Mukona', 'Todi')
for index, names in enumerate(name_list, start = 1):
    print(index,names)




person = {
    "name": "Zwivhuya",
    "age": 27,
    "gpa": 3.9,
    "Employee_id": 0,
    "Address": {
        "street": "Rixile street",
      "No": 2002,
      "town": "Makhado",
      "zip": "0920",
      "country": "South Africa",
      "suburb": "Tshikota Location"
    },
    "skills": ["Python","MongoDB","MySQL","Django","CSS & HTML","Docker"]
}

for key in person:
    if key == "skills":
        for skill in person["skills"]:
            print(skill)

for index, value in enumerate(person.items(), start = 1):
    print(index, value)