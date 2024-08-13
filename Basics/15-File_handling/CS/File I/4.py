name = input("Whats your name: ")

file = open("what.txt", "a")
file.write(f'{name}\n')
file.close()