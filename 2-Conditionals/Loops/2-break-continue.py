#Break: We use break when we like to get out of or stop the loop.

# syntax
#while condition:
#    code goes here
#    if another_condition:
#        break

count = 0
while count < 10:
    print(count)
    count += 1
    if count == 3:
        count += 1
        break
    