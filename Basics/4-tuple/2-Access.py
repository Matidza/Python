# Access tupple and Sclicing
tup = ('HTML', 'CSS', 'JS', 'React',
    'Redux', 'Node', 'MongDB',
    'Tomato', 'Potato', 'Cabbage',
    'Onion', 'Carrot'
)

print(tup[3])
print(len(tup))

# Sclicing

print(tup[:6])
print(len(tup[::6]))
print(tup[:6])
print(tup[0:7])
print(tup.count('HTML'))

lst = list(tup)
print(lst)