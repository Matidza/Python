#No: 1
def generate_full_name(first , last): # declaring a function
    space = ' '
    full_name = first + space + last 
    return full_name
print(generate_full_name("Zwivhuya", "Mukwevho")) # Calling a function

#NO: 2
def summation(num_one,num_two): # declaring a function
    total = num_one + num_two
    return total
print(summation(10,5)) # Calling a function

"""
lets try introducing
exceptions and user inputs
"""

#No: 3
def generate_full_name(first,last ): # declaring a function
    try:
        space = ' '
        full_name = first + space + last 
        return full_name
    except TypeError:
        print("Value enterd must be a string")

print(f"I'm {generate_full_name(input(str("Name: ")), input("Last name: "))}.") # Calling a function

# No: 4
def summation(num_one, num_two): # declaring a function
    try:
        total = num_one + num_two
        return f"The sum of num_one and num_two is {total}"   
    except TypeError:
        print("Value error occured!")
        print("Value entered is not an integer!")
print(summation( int(input("Number: ")) , int(input("Number: ")) )) # Calling a function

#No: 5 Age Calculator

# declaring a function with a parameters
def age_calculator(year_born, current_year):
    age = current_year - year_born
    return f"You are/ or turning {age} years old this year."
# Calling a function with arguments
print(age_calculator( 1997, 2024))