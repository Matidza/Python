name = input("Whats your name: ")

file = open("names.txt", "a")
file.write(name)
file.close

'''
a = appends data to the file, meaning data that is
    already in the txt file will not be remove, but new data
    will be add.

    but the problem is that all the data entered will be concantenated
    eg. ZWivhuyaMukonaWanga and not Zwivhuya Mukona Wanga
'''