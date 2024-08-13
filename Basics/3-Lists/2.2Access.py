info = ["Zwivhuya", "Mukwecho", "True",
        {
            "country": "South Africa",
            "City": "Vereeneging",
            "zip": "0920"
        },
        ['Python' , "MongoDB", "MySQL" ],'HTML', 'CSS', 'JS', 'React','Redux', 'Node', 'MongDB',
        'Tomato', 'Potato', 'Cabbage','Onion', 'Carrot'
]

print(info[2])
print(len(info[4]))
print(info[:4]) # all values till the 4th index
print(info[1:]) # start from the index 1
print(info[::3])
remove = info[12: 16]
veg = []
veg.append(remove)
print(f"This is a veg list {veg}")

info.insert(2, "years")
print(info[0])
