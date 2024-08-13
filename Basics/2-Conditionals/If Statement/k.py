A = int(input("Entre any number: "))
if A > 0 and A % 2 == 0:
    print("A is a positive and even integer")
elif A > 0:
    print("A is a positive integer")
elif A < 0:
    print("A is a negative integer")
else:
    print("A is equal to zero")