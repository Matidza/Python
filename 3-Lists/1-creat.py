# Create a List
#Syntax
# lst = list()

car = list()
print(len(car))

# With []
cars = []
print(len(cars))

# Lists with initial values. We use len() to find the length of a list.

fruits = ['banana', 'orange', 'mango', 'lemon']                     # list of fruits
vegetables = ['Tomato', 'Potato', 'Cabbage','Onion', 'Carrot']      # list of vegetables
animal_products = ['milk', 'meat', 'butter', 'yoghurt']             # list of animal products
web_techs = ['HTML', 'CSS', 'JS', 'React','Redux', 'Node', 'MongDB'] # list of web technologies
countries = ['Finland', 'Estonia', 'Denmark', 'Sweden', 'Norway']

print("fruits:", fruits)
print("Number of fruits are: ", len(fruits))
print(sep="")

print("vegetables:", vegetables)
print("Number of vegetables are: ", len(vegetables))
print(sep="")

print("animal products:", animal_products)
print("Number of animal products are: ", len(animal_products))
print(sep="")

print('Web technologies:', web_techs)
print('Number of web technologies:', len(web_techs))
print('Countries:', countries)
print('Number of countries:', len(countries))

## Unpacking List Items
veg = ['Tomato', 'Potato', 'Cabbage','Onion', 'Carrot']
v1, v2, v2, *rest = veg
print(v1)

##Accessing List Items Using Positive Indexing
veg = ['Tomato', 'Potato', 'Cabbage','Onion', 'Carrot']
print(veg[1])
print(len(veg) -1 )

## Accessing List Items Using Negative Indexing
# Slicing Items from a Listj
veg = ['Tomato', 'Potato', 'Cabbage','Onion', 'Carrot']