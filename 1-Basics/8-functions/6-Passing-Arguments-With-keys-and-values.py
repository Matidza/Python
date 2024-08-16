# DECLARING AND CALLING A FUNCTION
# WITH  TWO PARAMETERS
# THE ORDER OF ARGUMENTS  DOESN'T MATTER!!!!!!!
#Syntax

'''
def function_name(Para1, Para2): # Declaring a function
    code goes here
    code goes here

print(function_name(Para1 = "...", Para2 = "...")) # Calling a function
'''

# No: 1
def generate_full_name(first , last): # declaring a function
    space = ' '
    full_name = first + space + last 
    return full_name
print(generate_full_name(first = "Zwivhuya", last = "Mukwevho")) # Calling a function

#NO: 2
def summation(num_one,num_two): # declaring a function
    total = num_one + num_two
    return total
print(summation(num_one = 10, num_two = 5)) # Calling a function
