
try:
    available = int(input("Available raw material: "))
    required = int(input("Material required per unit: "))
    production = int(input("Planned production quantity: "))
    demand = int(input("Order demand: "))
    defects = int(input("Number of defective units: "))
    limit = float(input("Maximum defect rate (%): "))

    if min(available, required, production, demand, defects) < 0:
        raise ValueError("Values cannot be negative")
    if required == 0 or production == 0:
        raise ValueError("Material and production must be positive")
    if defects > production or not 0 <= limit <= 100:
        raise ValueError("Invalid defects or quality limit")

    material_needed = required * production
    shortage = max(0, material_needed - available)
    good_units = production - defects
    order_shortage = max(0, demand - good_units)
    defect_rate = defects / production * 100

    print("\n--- PRODUCTION REPORT ---")
    print("Material required:", material_needed)
    print("Material shortage:", shortage)
    print("Good units:", good_units)
    print("Order shortage:", order_shortage)
    print(f"Defect rate: {defect_rate:.2f}%")

    print("Production feasible:",
          "Yes" if shortage == 0 else "No")
    print("Quality status:",
          "Violation" if defect_rate > limit else "Acceptable")

except ValueError as e:
    print("Invalid input:", e)

