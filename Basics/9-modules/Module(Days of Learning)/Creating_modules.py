#Creating a nodule

#mymodule.py file

def generate_full_name(fist, last):
    return fist + " " + last

def summation(num_one, num_two): # declaring a function
    total = num_one + num_two
    return total


def summ(num_one = int(input("Number1: ")),num_two = int(input("Number2: "))): # declaring a function
    try:
        total = num_one + num_two
        return f"The sum of num_one and num_two is {total}"   
    except ValueError:
        print("Value error occured!")
        print("Value entered is not an integer!")
print(summ(  ))