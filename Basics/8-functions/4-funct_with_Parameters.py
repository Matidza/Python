#DECLARING AND CALLING A FUNCTION
#WITH PARAMETERS
'''

def function_name(Parameters): # Declaring a function
    code goes here
    code goes here


print(function_name(Arguments)) # Calling a function

'''
#No: 1
def greeting(name): # declaring a function with a parameter ("name")
    message = name + ", welcome to Python Learning"
    return message

print(greeting("Zwivhuya")) # Calling a function with argument("Zwivhuya")

#No: 2
def add(num):
    ten = 10
    return num + ten

print(add(int(input("What is your number: "))))

#No: 3
def square(x):
    return x * x

print(f'The square of x is: {square(int(input("What is x: ")))}')

#No: 4
def area_of_circle(r):
    PI = 3.14
    try:
        area = PI * r
        return area
    except TypeError:
        print(f"Value Error Occured!\n The value of r must be an integer!")
print(area_of_circle(int(input("Number: "))))