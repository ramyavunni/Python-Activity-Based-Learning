
name = input("Enter employee name: ")
basic = float(input("Enter basic salary: Rs. "))
allowances = float(input("Enter allowances: Rs. "))
overtime = float(input("Enter overtime pay: Rs. "))
incentives = float(input("Enter incentives: Rs. "))

gross = basic + allowances + overtime + incentives
if gross <= 20000:
    deduction = gross * 0.05
elif gross <= 40000:
    deduction = 20000 * 0.05 + (gross - 20000) * 0.10
else:
    deduction = (20000 * 0.05
                 + 20000 * 0.10
                 + (gross - 40000) * 0.15)

net = gross - deduction

print("\n------ SALARY STATEMENT ------")
print("Employee Name :", name)
print("Basic Salary  : Rs.", basic)
print("Allowances    : Rs.", allowances)
print("Overtime Pay  : Rs.", overtime)
print("Incentives    : Rs.", incentives)
print("Gross Salary  : Rs.", gross)
print("Deductions    : Rs.", deduction)
print("Net Salary    : Rs.", net)

