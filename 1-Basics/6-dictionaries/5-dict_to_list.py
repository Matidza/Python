person = {
    'first':'Asabeneh',
    'last':'Yetayeh',
    'age':250,
    'country':'Finland',
    'is_marred':True,
    'skills':['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address':{
        'street':'Space street',
        'zipcode':'02210'
    }
}

print(person.items()) #dictionary to list with its key value pair
print(person.keys()) # keys only to list
print(person.values())

person = {
    'first':'Asabeneh',
    'last':'Yetayeh',
    'age':250,
    'country':'Finland',
    'is_marred':True,
    'skills':['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address':{
        'street':'Space street',
        'zipcode':'02210'
    }
}

for index ,key in enumerate(person, start = 1 ):
    print( index, key)