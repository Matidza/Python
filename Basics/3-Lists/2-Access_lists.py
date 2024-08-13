# Access lists using Positive indexing

veg = ['Tomato', 'Potato', 'Cabbage','Onion', 'Carrot']

print(f"the second item in the list is a {veg[1]}")
print(f"the last item in the list is a {veg[-1]}")

#Unpacking
veg = ['Tomato', 'Potato', 'Cabbage','Onion', 'Carrot']
q,w,e, * rest = veg
print(q)
