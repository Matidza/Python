Months = input(str("What month is it? "))
if Months in ["January", "February", "March"]:
    term = "First term of the year"
elif Months in ["April", "May", "June"]:
    term = "Second term of the year"
elif Months in ["July", "August", "September"]:
    term = "Third term of the year"
elif Months in ["october", "November", "December"]:
    term = "Forth quarter of the year"
else:
    term = 'Invalid term'
print(f"{term}")

a = 6
if a >0 and a % 2 ==0:
    print("ok")

