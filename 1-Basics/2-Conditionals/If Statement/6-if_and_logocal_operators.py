user = "zwivhuya"
access_level = 3
if user == "admin" or access_level >= 4:
    print("Access granted")
else:
    print("Acces denied")