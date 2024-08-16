from statistics import *

ages = [20, 20, 4, 24, 25, 22, 26, 20, 23, 22, 26]

print(int(mean(ages)))
print(float(median(ages)))
print(mode(ages))
print(stdev(ages))

from random import *

random_user_id = [fd5bga5e4g5afd4bv5a4erga5fb48arg4t45ry4tr8h4a54g64erG5RG18RTERY465W8U47648687645Y4UW64U876534UWTR4]
for i in random(random_user_id):
    if i ==7:
        print(i)
        break

from requests import *