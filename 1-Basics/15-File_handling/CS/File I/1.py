# Writing into a file

name = input("Whats your name: ")

file = open("names.txt", "w")
file.write(name)
file.close

# This only writes and doent append to the 
# txt file if we where to run the script again
# thus it will remove the last entry and enter 
# the new one without appending.

'''
W = create a file and writes on the file
    re-creates a file whenever we run the script
'''