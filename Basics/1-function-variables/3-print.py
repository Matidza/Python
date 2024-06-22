#These are sone variables that we gonna use to utilise different types of data types and functions
#Functions = print(), type(), zip() etc
#Data types = str, int, float, bool, complex, list etc

first = "Zwivhuya"
last = "Mukwevho"
country = "South Africa"
age = 27
skills = ['Python','Figma','Django','CSS']
info = {
    'first_name': first,
    "last_name": last,
    "country": country,
    "age": age,
    "skills": skills
}

# No: 1
print(f"\n hello, i'm {first}")
print(f"Surname is {last}")
print(f"I'm from {country}")
print(f"I am {age} years old")
print(f"My skills include {skills}")
print(f"full details {info}")

#we can also optimize this with just one line
print(f"\n Hi, im {first} {last} and i am {age} years old\n" 
      "{country} is where I was bourn and raised\n"
      "My skills that I have obtained are {skills}\n")

print(f"This is my detailed info list({info})\n")
print(info)
print(list(info))
