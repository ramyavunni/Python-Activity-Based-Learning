
records = [
    "P101,2,500.00",
    "P102,5,1250.50",
    "P103,abc,300",
    "P104,3",
    "P105,2,-100"
]

print("INVOICE DATA EXTRACTION")

for record in records:
    try:
        fields = record.split(",")

        if len(fields) != 3:
            raise ValueError

        code = fields[0].strip()
        quantity = int(fields[1].strip())
        amount = float(fields[2].strip())

        if not code or quantity <= 0 or amount < 0:
            raise ValueError

        print(f"Code: {code}, Quantity: {quantity}, "
              f"Amount: Rs. {amount:.2f}")

    except ValueError:
        print(f"Malformed record: {record}")

