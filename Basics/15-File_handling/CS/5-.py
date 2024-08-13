name = input("Whats your name: ")

with open("what.txt", "a") as file:
    file.write(f'{name}\n')

'''
with = use to automaticaly open and close files
'''