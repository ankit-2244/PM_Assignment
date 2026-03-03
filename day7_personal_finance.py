"""
Day 7 PM Assignment: Personal Finance Calculator
Includes:
- Part A: Personal Finance Calculator
- Part B: Indian formatting
- Part C: Type analyzer + debug fixes
Author: Your Name
"""

# ====== Input Helpers ======
def get_float_input(prompt, min_value=None, max_value=None):
    """Ask user for float input and validate"""
    while True:
        try:
            value = float(input(prompt))
            if (min_value is not None and value < min_value) or \
               (max_value is not None and value > max_value):
                print(f"Enter a value between {min_value} and {max_value}.")
                continue
            return value
        except ValueError:
            print("Invalid input! Please enter a number.")

def get_employee_data():
    """Collect employee info with validation"""
    name = input("Employee Name: ").strip()
    annual_salary = get_float_input("Annual Salary (₹): ", min_value=0)
    tax_percent = get_float_input("Tax Bracket %: ", min_value=0, max_value=50)
    monthly_rent = get_float_input("Monthly Rent (₹): ", min_value=0)
    savings_percent = get_float_input("Savings Goal %: ", min_value=0, max_value=100)
    return name, annual_salary, tax_percent, monthly_rent, savings_percent

# ====== Calculation ======
def calculate_financials(annual_salary, tax_percent, monthly_rent, savings_percent):
    """Calculate monthly/annual financial metrics"""
    monthly_salary = annual_salary / 12
    monthly_tax = monthly_salary * (tax_percent / 100)
    net_salary = monthly_salary - monthly_tax
    rent_ratio = (monthly_rent / net_salary) * 100
    savings = net_salary * (savings_percent / 100)
    disposable_income = net_salary - (monthly_rent + savings)
    return {
        "monthly_salary": monthly_salary,
        "monthly_tax": monthly_tax,
        "net_salary": net_salary,
        "monthly_rent": monthly_rent,
        "rent_ratio": rent_ratio,
        "savings": savings,
        "disposable_income": disposable_income,
        "total_tax": monthly_tax*12,
        "total_savings": savings*12,
        "total_rent": monthly_rent*12
    }

# ====== Indian Number Format ======
def format_indian_number(n):
    """Format numbers in Indian lakh/crore style"""
    s = f"{int(n):,}"
    parts = s.split(',')
    if len(parts) <= 3:
        return '₹' + ','.join(parts)
    else:
        return '₹' + ','.join(parts[:-3] + [','.join(parts[-3:])])

# ====== Display Report ======
def display_report(name, tax_percent, fin):
    """Display formatted employee financial report"""
    print("═" * 45)
    print("EMPLOYEE FINANCIAL SUMMARY")
    print("═" * 45)
    print(f"Employee       : {name}")
    print(f"Annual Salary  : {format_indian_number(fin['monthly_salary']*12)}")
    print("─" * 45)
    print("Monthly Breakdown:")
    print(f"Gross Salary   : {format_indian_number(fin['monthly_salary'])}")
    print(f"Tax ({tax_percent:.1f}%)        : {format_indian_number(fin['monthly_tax'])}")
    print(f"Net Salary     : {format_indian_number(fin['net_salary'])}")
    print(f"Rent           : {format_indian_number(fin['monthly_rent'])} ({fin['rent_ratio']:.1f}% of net)")
    print(f"Savings ({tax_percent:.1f}%)   : {format_indian_number(fin['savings'])}")
    print(f"Disposable     : {format_indian_number(fin['disposable_income'])}")
    print("─" * 45)
    print("Annual Projection:")
    print(f"Total Tax      : {format_indian_number(fin['total_tax'])}")
    print(f"Total Savings  : {format_indian_number(fin['total_savings'])}")
    print(f"Total Rent     : {format_indian_number(fin['total_rent'])}")
    print("═" * 45)

# ====== Type Analyzer ======
def analyze_value(value):
    """Return value, type, truthiness, length"""
    try:
        length = len(value)
    except TypeError:
        length = "N/A"
    return f"Value: {value} | Type: {type(value).__name__} | Truthy: {bool(value)} | Length: {length}"

# ====== Debug Example ======
def debug_example():
    """Fixed debug code"""
    name = input("Name: ")
    age = int(input("Age: "))
    status = "Adult" if age >= 18 else "Minor"
    print(f"{name} is {age} years old and is a {status}")
    print(f"In 5 years: {age + 5}")
    score = 85.5
    print(f"Score: {score:.0f}")

# ====== MAIN ======
def main():
    """Run the assignment"""
    name, annual_salary, tax_percent, monthly_rent, savings_percent = get_employee_data()
    fin = calculate_financials(annual_salary, tax_percent, monthly_rent, savings_percent)
    display_report(name, tax_percent, fin)
    debug_example()

if __name__ == "__main__":
    main()