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