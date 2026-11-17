

order_id = "ORD-00742"
product = "Laptop"
region = "Khulna"
units_sold = 3
unit_price = 1104.24
discount_rate = 0.0
unit_cost = 662.04
customer_note = None
MAX_UNITS = 1000
REGIONS = ("Barishal", "Chattogram", "Dhaka", "Khulna", "Rajshahi", "Sylhet")

print("\n1. Arithmetic operators")
print(" Units + 2 =", units_sold + 2)
print("Price - cost =", round(unit_price - unit_cost, 2))
print("Units * price   =", (units_sold * unit_price, 2)) 
print("Price / units=", unit_price / units_sold)
print("\n2. Showing calculations ")
revenue = round(units_sold * unit_price * (1 - discount_rate), 2)
cost = round(units_sold * unit_cost, 2)
profit = round(revenue - cost, 2)
profit_margin = round(profit / revenue * 100, 2)
print(f"Revenue: {revenue:,.2f} BDT")
print(f"Cost:    {cost:,.2f} BDT")
print(f"Profit:  {profit:,.2f} BDT")
print(f"Margin:  {profit_margin:.2f} %")

print("\n3. Comparison operators")
print("product == 'Laptop'     ->", product == "Laptop")
print(" product != 'Desk ->", product != "Desk")
print("   unit_price > unit_cost  ->", unit_price > unit_cost)
print("unit_price < unit_cost =", unit_price < unit_cost)
print("units_sold >= 1         ->", units_sold >= 1)
print("units_sold <= MAX_UNITS ->", units_sold <= MAX_UNITS)

print("\n4. Logical operators")
is_valid_order = units_sold >= 1 and units_sold <= MAX_UNITS and unit_price > 0
is_discounted = discount_rate > 0
is_big_or_discounted = units_sold >= 5 or is_discounted
print("   Valid order (and)?        ", is_valid_order)
print("   Big or discounted (or)?   ", is_big_or_discounted)
print("   Full price (not)?         ", not is_discounted)

print("\n5. Assignment operators")
headphones_revenue = round(1 * 144.83 * (1 - 0.1), 2)
desk_revenue = round(5 * 207.13 * (1 - 0.0), 2)
running_total = 0
running_total += revenue
print(f"   After ORD-00742: {running_total:,.2f} BDT")
running_total += headphones_revenue
print(f"   After ORD-00879: {running_total:,.2f} BDT")
running_total += desk_revenue
print(f"   After ORD-00059: {running_total:,.2f} BDT")
running_total -= headphones_revenue
print(f"   Refund ORD-00879: {running_total:,.2f} BDT")
sales_target = 4000
sales_target *= 1.10
print(f"   Target raised 10 %: {sales_target:,.2f} BDT")


print("\n6. Percentage change")
january_revenue = 79360
february_revenue = 74408
percent_change = (february_revenue - january_revenue) / january_revenue * 100
print(f"   January:  {january_revenue:,.2f} BDT")
print(f"   February: {february_revenue:,.2f} BDT")
print(f"   Change:   {percent_change:.2f} %")