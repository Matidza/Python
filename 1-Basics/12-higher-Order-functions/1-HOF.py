# Higher Order Functions
#   

'''function as Parameters'''

def sum_numbers(nums): # normal function
    return sum(nums) # function using a buit-in function (sum)

def hof(f, lst):
    summation = f(lst)
    return summation

result = hof(sum_numbers, [1,2,3,4,5])
print(result)


def sum(x):
    return x + x
print(sum(3))

def hof(f,g):
    summ = f + g
    return summ
print(hof(2,sum(3)))


''' Returning Function  as Value/Argument'''
def square(x):
    return x ** 2  # square function

def cube(x):
    return x ** 3 # a cube function

def absolute(x):
    if x >= 0:
        return x
    else:
        return -(x)
    

# Now we use higher order function

def hof(type):
    if type == 'square':
        return square
    elif type == 'cube':
        return cube
    elif type == "absolute":
        return absolute
result = hof('square')
print(result(3))

resut = hof('cube')
print(resut(3))

resu = hof('absolute')
print(resu(-3))