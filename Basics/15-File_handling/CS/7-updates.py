# Update
# We want to Read the data in the file
# Open File
with open('names.txt', "r") as file:
    for line in file:
        print("hello, ", line.rstrip())


#Sorted - sorting all the data before being printed
with open('names.txt', "r") as file:
    for line in sorted(file, reverse=True):
        print("hello, ", line.rstrip())


#Sorted and Indexed
with open('names.txt', "r") as file:
    for index, line in enumerate (sorted(file, reverse=True), start=1):
        print(index, line.rstrip())


        