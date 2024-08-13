# IMPORTING MODULES

import Creating_modules

print(Creating_modules.generate_full_name("zwovhuya", "Mukwevho"))

from Creating_modules import generate_full_name

print(generate_full_name("Zwivhuya","Mukwevho"))

print(Creating_modules.summation(12,42))

print(Creating_modules.summ())

import os
os.mk("what.py")
print(os.getcwd())

import sys
print("Welcome {}. Enjoy {} challenge!".format(sys.argv[1], sys.argv[2]))