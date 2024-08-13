# RETURNING A VALUE
# WITHOUT A PARAMETER

#No: 1
def generate_full_name(): # declaring a function
    first = "Zwivhuya"
    last = "Mukwevho"
    space = ' '
    full_name = first + space + last 
    return full_name
print(generate_full_name()) # Calling a function

#NO: 2
def summation(): # declaring a function
    num_one = 10
    num_two = 5
    total = num_one + num_two
    return total
print(summation()) # Calling a function

"""
lets try introducing
exceptions and user inputs
"""

#No: 3
def generate_full_name(): # declaring a function
    try:
        first = input(str("Name: "))
        last = input("Last name: ")
        space = ' '
        full_name = first + space + last 
        return full_name
    except TypeError:
        print("Value enterd must be a string")

print(f"I'm {generate_full_name()}.") # Calling a function

# No: 4
def summation(): # declaring a function
    try:
        num_one = int(input("Number: "))
        num_two = int(input("Number: "))
        total = num_one + num_two
        return f"The sum of num_one and num_two is {total}"
    except ValueError:
        print("Value error occured!")
        print("Value entered is not an integer!")
print(summation()) # Calling a function