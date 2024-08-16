# Access a set
set = {
    'HTML', 'CSS', 'JS', 'React',
    'Redux', 'Node', 'MongDB',
    'Tomato', 'Potato', 'Cabbage',
    'Onion', 'Carrot'
}
print("CSS" in set) # Checking item in sets

# Adding item in set
set.add("Zwivhuya") # Add one item
set.update(['Wanga', "Mukona", "Todani", "Michelle"])
print(set)

# Removing items
set.remove("Zwivhuya")
print(set)
print(set.pop())