#While loops

#We use the reserved word while to make a while loop.
# It is used to execute a block of statements repeatedly until a given condition 
# is satisfied. When the condition becomes false, the lines of code after the loop 
# will be continued to be executed.

# Syntax
# While condition:
#     code goes here

#No 1 :

count = 1
while count <= 5:
    print(count)
    count += 1
    

# syntax
# while condition:
#     code goes here
# else:
#    code goes here

aim = 0
while aim < 10:
    print(aim)
    aim += 1
else:
    print(aim)