# Day 2:30 Days of python programming
first_name = "Zwivhuya"
last_name = "Mukwevho"
full_name = first_name + last_name
country = "South Africa"
city = "Gauteng"

age = 27
year = 2024
is_married = False
is_true = "yes"
info = {
    'first_name': first_name,
    "last_name": last_name,
    "country": country,
    "age": age 
}

#Exercise Level 2:
# 1: Checking the data types of all the variables
print(type(first_name))
print(type(last_name))
print(type(full_name))
print(type(first_name))
print(type(age))
print(type(is_married))
print(type(info))

#Using the len() built-in function, find the length of your first name
print(len(first_name))

#Compare the length of your first name and your last name
print(len(first_name))
print(len(last_name))

#Declare 5 as num_one and 4 as num_two
num_one = 5
num_two = 4

#Add num_one and num_two and assign the value to a variable total

total = num_one + num_two
print(total)

diff = num_two - num_one
print(diff)

product = num_one * num_two
print(product)

division = num_one/num_two # division
print(division)

expo = num_one**num_two # power
print(expo)

remainder = num_one%num_two # remainder division
print(remainder)

floor_division = num_one//num_two # floor division
print(floor_division)

#The radius of a circle is 30 meters.
radius = 30
pie = 3.14
area_of_circle = pie * (radius**2)
print(f"area_of_circle is {area_of_circle}")

circum = 2 * pie * radius
print(circum)

r = int(input("Radius = "))
area = pie * (r**2)
print(f"Area is", area)