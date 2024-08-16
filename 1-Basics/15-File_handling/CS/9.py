import json
person_json = """{
    "first":"Asabeneh",
    "last":"Yetayeh",
    "age":250,
    "country":"Finland",
    "is_marred":True,
    "skills":["JavaScript", "React", "Node", "MongoDB", "Python"],
    "address":{
        "street":"Space street",
        "zipcode":"02210"
    }
}"""

pers = json.loads(person_json)
print(pers)