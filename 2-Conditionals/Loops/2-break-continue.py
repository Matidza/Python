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
#The above while loop only prints 0, 1, 2, but when it reaches 3 it stops.

  # syntax
# while condition:
#     code goes here
#     if another_condition:
#         continue

aim = 0
while aim < 8:
    if aim == 3:
        aim += 1
        continue
    print(aim)
    aim += 1
#The above while loop only prints 0, 1, 2 and etc (skips 3).
one = 0
while one < 20:
    print(one)
    one += 1
    if one == 10:
        one += 1
        break
    
one = 0
while one < 20:
    if one == 10:
        break
    print(one)
    one += 1