from datetime import datetime

now = datetime.now()
print(f"\n {now} \n")

day = now.day
month = now.month
year = now.year
hour = now.hour
minute = now.minute
second = now.second
timestamp = now.timestamp()
print(f"{day}/{month}/{year}")
print(f"Timestamp: {timestamp}")