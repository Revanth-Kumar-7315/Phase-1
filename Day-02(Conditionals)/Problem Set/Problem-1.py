"""
📝 Description:
Ask the user for their annual salary and compute tax based on the following slab:

- Up to ₹2.5L: No Tax
- ₹2.5L–5L: 5%
- ₹5L–10L: 20%
- ₹10L+: 30%
🔧 Tasks:
Use float(input()) and round the final tax.
Print both the taxable amount and tax owed.
Add input validation: if user types negative salary, print error.
"""

Annual_Salary = float(input("Enter your annual salary : "))

if Annual_Salary < 0:
    print("Error: Salary cannot be negative.")
elif Annual_Salary <= 250000:
    print("No Tax required to pay")
    print(f"Taxable amount: ₹0")
    print(f"Tax owed: ₹0")
elif 250000 < Annual_Salary <= 500000:
    taxable_amount = Annual_Salary - 250000
    Tax_owed = round(taxable_amount * 0.05)
    print(f"Taxable amount: ₹{taxable_amount}")
    print(f"Tax owed: ₹{Tax_owed}")
elif 500000 < Annual_Salary <= 1000000:
    taxable_amount = Annual_Salary - 500000
    Tax_owed = round(250000 * 0.05 + taxable_amount * 0.2)
    print(f"Taxable amount: ₹{Annual_Salary - 250000}")
    print(f"Tax owed: ₹{Tax_owed}")
elif 1000000 < Annual_Salary:
    taxable_amount = Annual_Salary - 1000000
    Tax_owed = round(250000 * 0.05 + 500000 * 0.2 + taxable_amount * 0.3)
    print(f"Taxable amount: ₹{Annual_Salary - 250000}")
    print(f"Tax owed: ₹{Tax_owed}")
