#Conditionals

# If condition
#syntax: if condition:
#               this part of code runs for truthy conditions

#No 1: 
a = 5
if a > 0:
    print("\nA is a positive number \n")
    
#If Else conditions
# syntax
#  if condition:
#     this part of code runs for truthy conditions
#  else:
#     this part of code runs for false conditions

b = 10
if b < 0:
    print("B is a negative number\n")
else:
    print("B is a positive number\n")

# syntax
#if condition:
    #code
#elif condition:
#    code
#else:
#    code

A = 0
if A < 0:
    print("A is a negative number")
elif A > 0:
    print("A is a positive number")
else:
    print("A is zero")
    
    # syntax
#code if condition else code

A = 0
print("A is positive") if A > 0 else print("A is negative")

#Nested Conditions

a = 2 
if a > 0:
    if a % 2 == 0:
        print("A is an even number that is positive")
    else:
        print("A is a positive number")
elif a == 0:
    print("A is zero")
else:
    print("A is a negative number")
    
    
a = 0
if a > 0 and a % 2 ==0:
    print("A is a positive and even number")
elif a > 0:
    print("A is positive")
elif a == 0:
    print("A is zero")
else:
    print("A is a negative number")
    
user = "zwivhuya"
access_level = 3
if user == "admin" or access_level >= 4:
    print("Access granted")
else:
    print("Acces denied")