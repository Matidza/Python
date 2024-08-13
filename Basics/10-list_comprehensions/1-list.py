"""
List comprehension is a short way of creating 
a list. they are faster at proccessing a list than using the for
loop
"""



cars = ['Audi', 'BMW', 'VW', 'Mazda']
for index,i in enumerate(cars, start= 1):
    print(index, i)

# Syntax
# [ i for iterable if condition]
'''
    now using comprehensions
''' 
cars = ['Audi', 'BMW', 'VW', 'Mazda'] 
car = [i for  i in cars]
print(car)

# No: 2
numbers = range(11)
number = [i for i in numbers]
print(number)



number = [i for i in range(16) if i <= 10 ]
print(number)

#even number
number = [i for i in range(16) if i %2 == 0 ]
print(number)

#not even
number = [i for i in range(16) if i %2 !=0 ]
print(number)

even = [-9,-8,-7,-6,-5,-4,-3,-2,-1,0,1,2,3,4,5,6,7,8,9]
number = [i for i in range(21) if i %2 ==0 and i > 0 ]
print(number)

number = [i for i in range(16) if i  == 6 ]
print(number)

even = [-9,-8,-7,-6,-5,-4,-3,-2,-1,0,1,2,3,4,5,6,7,8,9]
number = [i for i in even[0: 11]  ]
print(number)


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
info = [i for i in person['country']]
print(info)

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
info = [i for i in person['skills'] if i == "JavaScript"]
print(info)


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
info = [i for i in person['address']['street']]
print(tuple(info))

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
info = [i for i in person['skills'][1:]]
print(info)