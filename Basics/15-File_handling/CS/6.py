# We want to Read the data in the file
# Open File
with open('names.txt', "r") as file:
    lines = file.readlines()

for line in lines:
    print("hello, ", line.rstrip())