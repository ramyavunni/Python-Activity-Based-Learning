
import math
from datetime import datetime

rates = {"bike": 20, "car": 50, "truck": 80}

try:
    vehicle = input("Vehicle (bike/car/truck): ").lower()
    entry = datetime.strptime(input("Entry time (HH:MM): "), "%H:%M")
    exit_time = datetime.strptime(input("Exit time (HH:MM): "), "%H:%M")

    if vehicle not in rates:
        raise ValueError("Invalid vehicle category")

    start = entry.hour * 60 + entry.minute
    end = exit_time.hour * 60 + exit_time.minute
    duration = end - start

    if duration < 0:
        duration += 1440
    elif duration == 0:
        raise ValueError("Entry and exit times cannot be equal")

    hours = math.ceil(duration / 60)
    fee = min(hours * rates[vehicle], 300)
    penalty = 50 if end < start else 0

    print("\nParking duration:", hours, "hours")
    print("Base fee: Rs.", fee)
    print("Penalty: Rs.", penalty)
    print("Total fee: Rs.", fee + penalty)

except ValueError as e:
    print("Error:", e)

