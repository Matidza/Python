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

# Access items through keys

print(person['first'])
print(person['address'])

print(person['skills'][:3]) # even slicing
print(person['address']['street'])

# Using get() method
print(person.get('City'))

# Adding items and values
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


person['skills'].append('MySQL') # Adding a value to a list in a dic
person['city'] = 'polokwane' # adding a key and value 
person['address']["town"] = "Makhado" # adding a key and value to a dictionay in a dictionary
print(person)

