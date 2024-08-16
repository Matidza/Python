tup = ('HTML', 'CSS', 'JS', 'React',
    'Redux', 'Node', 'MongDB',
)
tup2 = ('Tomato', 'Potato', 'Cabbage',
    'Onion', 'Carrot'
)

tup.append("Whats next")
print(tup)

tup3 = tup + tup2
print(tup3)

veges = tup[7::]
print(veges)

# Deleting tuples
del tup
print(tup)
