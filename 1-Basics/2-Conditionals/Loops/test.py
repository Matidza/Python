#Exercises: Level 1

# Iterate 0 to 10 using for loop, do the same using while loop.



# Write a loop that makes seven calls to print(),
# so we get on the output the following triangle:

#No 1:
number = [0,1,2,3,4,5,6,7,8,9,10]
for i in number:
    print(i)
    
for i in range(11):
    print(i)

count = 0
while count < 11:
    print(count)
    count += 1
# Iterate 10 to 0 using for loop, do the same using while loop.  
count = 10
while count < 12:
    if count < 0:
        break
    print(count)
    count -= 1

number = [10,9,8,7,6,5,4,3,2,1,0]
for i in number:
    print(i)
    
# Write a loop that makes seven calls to print(),
# so we get on the output the following triangle:
text = "#"
for i in text:
    print(i*text)
    text += 1
    
for i in range(1, 11):
    print(i* '#')
for i in range(11):
    print(i)