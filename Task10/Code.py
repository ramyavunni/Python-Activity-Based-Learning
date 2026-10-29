
apartments = []

n = int(input("Number of apartments: "))

for i in range(n):
    aid = input("Apartment ID: ")
    units = int(input("Units consumed: "))
    reported = float(input("Reported bill: "))

    if units < 0 or reported < 0:
        print("Invalid input!")
        continue

    # Progressive tariff
    energy = (min(units, 100) * 2
              + min(max(units - 100, 0), 100) * 3
              + max(units - 200, 0) * 5)

    bill = energy + 100  # Fixed charge

    rebate = bill * 0.05 if units <= 100 else 0
    bill -= rebate

    discrepancy = abs(bill - reported) > 1

    apartments.append((aid, units, bill, reported, discrepancy))

apartments.sort(key=lambda x: x[1], reverse=True)

print("\n--- ELECTRICITY BILLING REPORT ---")
for rank, (aid, units, bill, reported, diff) in enumerate(apartments, 1):
    print(f"\nRank: {rank} | Apartment: {aid}")
    print("Units:", units)
    print(f"Calculated bill: Rs. {bill:.2f}")
    print(f"Reported bill: Rs. {reported:.2f}")
    print("Discrepancy:", "Yes" if diff else "No")

