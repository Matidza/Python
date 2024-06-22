# For loop with list
# syntax

#for iterator in lst:
#    code goes here

numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
for number in numbers:
    print( number)
    
# For loop with string
# syntax 
# for interator in string:
#       code goees here

names = "Zwivhuya"
for index, name in enumerate(names, start = 1):
    print(index, name)
    
language = "python"
for i in range(len(language)):
    print(language[i])
    
# For loop with tuple
# syntax
# for iterator in tpl:
#     code goes here

number = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
for index, i in enumerate(number, start = 1):
    print(index, i)
    
# For loop with dictionary
# syntax
# for iterator in dic:
#     code goes here

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

for key in person:
    print(key)
    
for key, value in person.items():
    print(key, value)



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
sc = ["School"]
year = ["NWU"]
city = ['Province', 'town']
value = ['Gauteng', 'Vereeneging']
for i in range(len(sc)):
    person[sc[i]] = year[i]
for r in range(len(city)):
    person['address'][city[r]] = value[r]
print(person)

# For loop with sets
# syntax
# for iterator in sets:
#     code goes here

companies = {'Facebook', 'Google', 'Microsoft',
             'Apple', 'IBM', 'Oracle', 'Amazon'}
for com in companies:
    print(com)
    
