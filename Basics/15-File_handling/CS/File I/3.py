name = input("Whats your name: ")

file = open("names.txt", "a")
file.write(f'{name}\n')
file.close()

'''
a = appends data to the file, meaning data that is
    already in the txt file will not be remove, but new data
    will be add.
    Now that we have added a new line after ever data entered
    there will be no concantenated data
    eg.
    Zwivhuya
    Mukona
    Wanga
'''