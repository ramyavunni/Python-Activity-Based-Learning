
import math

try:
    venue = float(input("Enter venue cost: "))
    equipment = float(input("Enter equipment cost: "))
    catering = float(input("Enter catering cost per participant: "))
    transport = float(input("Enter transport cost: "))
    certificate = float(input("Enter certificate cost per participant: "))
    sponsorship = float(input("Enter sponsorship amount: "))
    contribution = float(input("Enter contribution per participant: "))
    participants = int(input("Enter expected participants: "))

    if min(venue, equipment, catering, transport,
           certificate, sponsorship, contribution) < 0:
        raise ValueError("Costs and funding cannot be negative")
    if participants <= 0 or contribution <= 0:
        raise ValueError("Participants and contribution must be positive")

    fixed_cost = venue + equipment + transport
    variable_cost = catering + certificate
    total_cost = fixed_cost + variable_cost * participants
    shortfall = max(0, total_cost - sponsorship)
    required_per_person = shortfall / participants

    if contribution > variable_cost:
        breakeven = max(0, math.ceil(
            (fixed_cost - sponsorship) /
            (contribution - variable_cost)
        ))
    else:
        breakeven = (
            0 if sponsorship >= fixed_cost else None
        )

    print("\n--- CAMPUS EVENT FINANCIAL REPORT ---")
    print("Total event cost: Rs.", round(total_cost, 2))
    print("Sponsorship: Rs.", round(sponsorship, 2))
    print("Sponsorship shortfall: Rs.", round(shortfall, 2))
    print("Required contribution per participant: Rs.",
          round(required_per_person, 2))
    print("Break-even registrations:",
          breakeven if breakeven is not None
          else "Not achievable at this contribution")

except ValueError as e:
    print("Invalid input:", e)

