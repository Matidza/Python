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


count = 1
while count <= 10:
    print(count)
    count += 1
    if count == 5:
        count += 1
        break

count = 1
while count < 10:
    if count == 5:
        count += 1
        continue
    print(count)
    count += 1

count = 1
while count <=20:
    print(count)
    count += 1
    if count == 10:
        count += 1
        continue

one = (1,2,3,4,5,6,7,8,9)
for i in one:
    if i == 5:
        continue
    print(i)


one = 1
while one <= 10:
    if one == 5:
        one += 1
        continue
    print(one)
    one += 1

