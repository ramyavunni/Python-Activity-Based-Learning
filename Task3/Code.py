import math
from datetime import datetime

rates = {"bike": 20, "car": 50, "truck": 80}

try:
    vehicle = input("Enter vehicle (bike/car/truck): ").lower()
    entry = input("Enter entry time (HH:MM): ")
    exit_time = input("Enter exit time (HH:MM): ")

    start = datetime.strptime(entry, "%H:%M")
    end = datetime.strptime(exit_time, "%H:%M")

    if vehicle not in rates:
        raise ValueError("Invalid vehicle category")

    duration = (end.hour * 60 + end.minute) - \
               (start.hour * 60 + start.minute)

    if duration < 0:
        duration += 1440
    elif duration == 0:
        raise ValueError("Entry and exit times cannot be equal")

    hours = math.ceil(duration / 60)
    fee = min(hours * rates[vehicle], 300)

    overnight = end < start
    penalty = 50 if overnight else 0
    total = fee + penalty

    print("\nParking duration:", hours, "hours")
    print("Base fee: Rs.", fee)
    print("Overnight penalty: Rs.", penalty)
    print("Total parking fee: Rs.", total)

except ValueError as e:
    print("Error:", e)
