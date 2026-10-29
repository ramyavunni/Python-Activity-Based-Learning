
participants = []
seen = set()
duplicates = []

n = int(input("Enter number of registrations: "))

for i in range(n):
    pid = input("Enter participant ID: ")
    fee = float(input("Enter registration fee: "))

    if pid in seen:
        duplicates.append(pid)
    else:
        seen.add(pid)
        participants.append(fee)

sponsorship = float(input("Enter total sponsorship: "))
expenses = float(input("Enter total expenses: "))

registration_total = sum(participants)
total_income = registration_total + sponsorship
balance = total_income - expenses

print("\n--- FESTIVAL FINANCIAL AUDIT ---")
print("Valid registrations:", len(participants))
print("Duplicate IDs:", duplicates)
print("Registration fees: Rs.", registration_total)
print("Sponsorship: Rs.", sponsorship)
print("Total income: Rs.", total_income)
print("Total expenses: Rs.", expenses)
print("Final balance: Rs.", balance)

if balance > 0:
    print("Status: Surplus")
elif balance < 0:
    print("Status: Deficit")
else:
    print("Status: Balanced")

