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
print("A is positive") if A > 0 elif print("A is negative") if A < 0 else print("A is equal to zero")