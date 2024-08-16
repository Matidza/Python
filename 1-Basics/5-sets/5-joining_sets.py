set_1 = {
    'HTML', 'CSS', 'JS', 'React',
    'Redux', 'Node', 'MongDB'
}

set_2 = {
    'Tomato', 'Potato', 'Cabbage',
    'Onion', 'Carrot'
}

# Joing sets
#    union()
#    update()

all_sets = set_1.union(set_2)
print(all_sets)

set_2.update(set_1) # Content in set_1 will be added in set_2 insert a set into a set
print(set_2)

set_2 = {
    'Tomato', 'Potato', 'Cabbage',
    'Onion', 'Carrot'
}
print(set_2.clear())