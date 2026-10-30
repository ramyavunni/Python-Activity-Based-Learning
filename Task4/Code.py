
n = int(input("Enter number of locations: "))

for i in range(n):
    print("\nLocation", i + 1)

    name = input("Enter location name: ")
    received = int(input("Quantity received: "))
    distributed = int(input("Quantity distributed: "))
    damaged = int(input("Quantity damaged: "))
    actual = int(input("Actual remaining stock: "))
    minimum = int(input("Minimum required stock: "))

    expected = received - distributed - damaged
    discrepancy = expected - actual
    replenish = max(0, minimum - actual)

    print("\n--- Stock Report ---")
    print("Location:", name)
    print("Expected Stock:", expected)
    print("Actual Stock:", actual)
    print("Discrepancy:", discrepancy)

    if discrepancy == 0:
        print("Status: Stock Matched")
    elif discrepancy > 0:
        print("Status: Stock Shortage")
    else:
        print("Status: Extra Stock")

    print("Replenishment Required:", replenish)
