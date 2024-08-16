# Create a List
#Syntax
# lst = list()

my_list = list()
print(len(my_list))

fruits = ['banana', 'orange', 'mango', 'lemon']                     # list of fruits
vegetables = ['Tomato', 'Potato', 'Cabbage','Onion', 'Carrot']      # list of vegetables
animal_products = ['milk', 'meat', 'butter', 'yoghurt']             # list of animal products
web_techs = ['HTML', 'CSS', 'JS', 'React','Redux', 'Node', 'MongDB'] # list of web technologies
countries = ['Finland', 'Estonia', 'Denmark', 'Sweden', 'Norway']
print(fruits.index('orange'))
one = fruits.extend(vegetables)
print(one)

print(f"\n the length of the list is {len(fruits)}.\n", fruits, sep="")
print(f"\n the length of the list is {len(vegetables)}.\n", vegetables, sep="")
print(f"\n the length of the list is {len(animal_products)}.\n", animal_products, sep="")
print(f"\n the length of the list is {len(web_techs)}.\n", web_techs, sep="")
print(f"\n the length of the list is {len(countries)}.\n", countries, sep="")

#different items in a list
info = ["Zwivhuya", "Mukwecho", "True",
        {
            "country": "South Africa",
            "City": "Vereeneging",
            "zip": "0920"
        },
        ['Python' , "MongoDB", "MySQL" ]
]
REMOVE = info[3:: ]
print(REMOVE.copy())

print(f"\n the length of the list is {len(info)}.\n", info, sep="")
print(info.sort(reverse=True))