"""
    try:
        code goes here
    except:
        code in this block run if things go wrong

"""
#No: 1
try:
    print(10 + "5")
except:
    print("Something went wrong")

# No: 2
try:
    name = input("Enter your name: ")
    year_born =  input('Year you were born: ')
    age = 2024 - year_born
    print(f"You are {name}. And your age is {age}")
except:
    print("Something went wrong")


#No: 3
try:
    name = input("Enter your name: ")
    year_born =  int(input('Year you were born: '))
    age = 2024 - year_born
    print(f"You are {name}. And your age is {age}")
except TypeError:
    print("Type error occured")
except ValueError:
    print("Value error occured")
    print("Value entered must be an integer")
except ZeroDivisionError:
    print("Zero divission error occured!")
    print("Age doesn't compute!")