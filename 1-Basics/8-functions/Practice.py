# Functions are re-usable piece/block of 
# code designed to perform a task.
# To define/declare a function we use ( def () )
# But the fuction also needs to be called


# Syntax
# def function name():
#           code goes here
#           code goes here

# function name() """ This is calling the function"""

"""
Example: 1 Declaring and Calling a function
"""
# 

"""1a: With no parameters"""
def generate_full_name():
    # inside the function
    name = "Zwivhuya"
    surname = "Mukwevho"
    full_name = name + " " + surname
    print(full_name)

generate_full_name() # Calling the function outside the def function


def summation():
    num_1 = 10
    num_2 = 4
    total = num_1 + num_2
    print(total)

summation() 

"""1b :With no parameters and returning a value Part 1"""

def generate_full_name():
    name = input("Name: ")
    surname = input("Surname: ")
    space = " "
    full_name = name + space + surname
    return f"{full_name}"
print(generate_full_name())

def summation():
    num_1 = int(input("What is your number:"))
    num_2 = int(input("What is your other number: "))
    total = num_1 + num_2
    return f"sum of num_1 and num_2 is {total}"
print(summation())



"""
Example: 2 Declaring and Calling a function
With One Parameter (para_1)
"""

def greet(name):
    message = f"how are you this morning {name} "
    return message

print(greet("Zwivhuya"))

def summation(num):
    ten = 10
    sum = num + ten
    return sum
print(summation(2))
# Update of above
def summation(num):
    ten = 10
    sum = num + ten
    return sum
num = int(input("num: "))
print(summation(num))

def square(x):
    return x * x

print(square(5))

# update of above
def square(x):
    
    return x * x

print(square(x = int(input("What is x value: ", ))))

def area(r):
    PI = 3.14
    A = PI * r ** 2
    return f" Area of the circle is {A}"
r = int(input("radius of the circle is: "))
print(area(r))



"""
Example:  Declaring and Calling a function
With Two Parameters (para_1, para_2)
"""

def generate_full_name(name, last):
    full_name = name + " " + last
    return full_name
print(generate_full_name("Zwivhuya", "Mukwevho"))


def sum_two_numbers (num_one, num_two):
    sum = num_one + num_two
    return sum
print('Sum of two numbers: ', sum_two_numbers(1, 9))

def weight_of_object (mass, gravity):
    weight = str(mass * gravity)+ ' N' # the value has to be changed to a string first
    return weight
print('Weight of an object in Newtons: ', weight_of_object(100, 9.81))