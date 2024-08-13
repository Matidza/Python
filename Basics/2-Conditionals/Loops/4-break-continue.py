# Break and Continue - Part 2

# syntax
#for iterator in sequence:
#    code goes here
#    if condition:
#        break
#BREAK
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
for num in numbers:
    if num == 5:
        num += 1
        break
    print(num)
    num += 1
    
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
for num in numbers:
    if num == 5:
        print(num)
        break
        
    
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
for num in numbers:
    print(num)
    if num == 5:
        break
    
    
#Continue
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
for num in numbers:
    if num == 5:
        continue
    print(num)
    
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
for num in numbers:
    print(num)
    if num == 5:
        continue
    
numbers = (0,1,2,3,4,5)
for number in numbers:
    print(number)
    if number == 3:
        continue
    print('Next number should be ', number + 1) if number != 5 else print("loop's end") # for short hand conditions need both if and else statements
print('outside the loop')

for number in range(11):
    if number == 4:
        break
    print(number)


lst = list(range(1,10,3))
print(lst)