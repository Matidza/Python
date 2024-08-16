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