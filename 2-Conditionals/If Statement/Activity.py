#Exercises: Level 1
#No 1
#Get user input using input(“Enter your age: ”).
# If user is 18 or older, give feedback: You are old enough to drive.
# If below 18 give feedback to wait for the missing amount of years.

age = int(input("Enter your age: "))
if age >= 18:
    print("You are old enough to drive.")
else:
    print("You need 3 more years to learn to drive")
    
#Get two numbers from the user using input prompt.
# If a is greater than b return a is greater than b, if a is 
# less b return a is smaller than b, else a is equal to b.

num1 = int(input("Enter number one: "))
num2 = int(input("Enter number two: "))
if num1 > num2:
    print(f"{num1} is greater than {num2}")
else :
    print(f"{num2} is less that {num1}")
    
#Write a code which gives grade to students according to theirs scores:
#80-100, A
#70-89, B
#60-69, C
#50-59, D
#0-49, F

Grade = int(input("Enter your grade: "))
if Grade >= 80:
    print(" A")
elif Grade >= 70 <= 79:
    print("B")
elif Grade >= 60 <= 69:
    print("C")
elif Grade >= 50 <= 59:
    print("D")
else:
    print("F")
    
#Check if the season is Autumn, Winter, Spring or Summer.
# If the user input is: September, October or November, the season is Autumn.
# December, January or February, the season is Winter.
# March, April or May, the season is Spring
# June, July or August, the season is Summer


month = input(str("What month is it? "))
if month in ["September", "October", "November"]:
    season = 'Autumn'
elif month in ["December", "January", "February"]:
    season = 'Winter'
elif month in ["March", "April", "May"]:
    season = "Spring"
elif month in ["June", "July", "August"]:
    season = "Summer"
else:
    season = 'Invalid month'
print(f"The season is {season}")
