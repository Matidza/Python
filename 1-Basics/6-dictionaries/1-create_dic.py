# creating a Dictionary
dic = {}

person = {
    'first':'Asabeneh',
    'last':'Yetayeh',
    'age':250,
    'country':'Finland',
    'is_marred':True,
    'skills':[
        {'street':'Space street',
        'zipcode':'02210'
        }]
}

for result in person["skills"]:
    print(result["street"])

person = {
    'first':'Asabeneh',
    'last':'Yetayeh',
    'age':250,
    'country':'Finland',
    'is_marred':True,
    'skills':['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address':
        {
        'street':'Space street',
        'zipcode':'02210'
        }
}
print(person["address"]["street"])

person = {
    'first':'Asabeneh',
    'last':'Yetayeh',
    'age':250,
    'country':'Finland',
    'is_marred':True,
    'skills':['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address':
        {
        'street':'Space street',
        'zipcode':'02210'
        }
}

print(f"\n The length of the dictionary is {len(person)}:")
print(f"{person}\n")

for key in person:
    print(f"{key}", sep=" ") # printing keys only
for key, value in person.items():
    print(f"{key}, {value}", sep=" ") # printing keys and values

for key, value in person.items():
    print(value) #printing values only