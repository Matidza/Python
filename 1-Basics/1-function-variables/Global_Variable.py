"""
Global variable outside
the def function
"""
x = "Zwivhuya"
def function():
    print(f"My name is {x}")
function()

"""
Global variables both 
in and outside the def function
"""
y = "Mukwevho"
def surname():
    y = "Fantastic"
    print("My surname is " + y)

surname()

print("This is my surname by the way: " + y)


"""
If you use the global keyword,
the variable belongs to the global scope:
"""

def name():
    global x
    x = "Zwivhuya"
    y = print(f"{x} is my name")
    return y
name()
