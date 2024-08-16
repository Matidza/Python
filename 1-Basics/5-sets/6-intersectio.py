# Finding intersecting items
set_1 = {
    'HTML', 'CSS', 'JS', 'React','Redux', 'Node', 'MongDB'
}

set_2 = {
    'Tomato', 'Potato', 'Cabbage','Onion', 'Carrot','HTML', 'CSS','MongDB','React','Redux', 'Node',
}

set_1.intersection(set_2)
print(set_1)

#checking Subsets and supersets



print(set_2.issubset(set_1))
print(set_1.issuperset(set_2))

print(set_2.issuperset(set_1))
print(set_1.issubset(set_2))

# Checking the difference between two sets
print(set_2.difference(set_1))
print(set_1.difference(set_2))

# Finding Symatric Difference Between two sets

print(set_2.symmetric_difference(set_1))