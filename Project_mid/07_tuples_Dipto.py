
CATEGORIES = ("Electronics", "Furniture", "Appliances", "Stationery", "Accessories")
REGIONS = ("Barishal", "Chattogram", "Dhaka", "Khulna", "Rajshahi", "Sylhet")
DISCOUNT_RATES = (0.0, 0.05, 0.10, 0.15, 0.20)

orders = [
    ("ORD-00742", "Laptop", "Khulna", 3, 1104.24, 0.0),
    ("ORD-00879", "Headphones", "Sylhet", 1, 144.83, 0.1),
    ("ORD-00059", "Desk", "Sylhet", 5, 207.13, 0.0),
    ("ORD-00628", "Office Chair", "Sylhet", 1, 168.07, 0.1),
    ("ORD-00874", "Laptop", "Sylhet", 8, 962.66, 0.0),
    ("ORD-00594", "Smartphone", "Barishal", 6, 269.73, 0.1),
    ("ORD-00145", "Printer Paper", "Dhaka", 4, 11.74, 0.05),
    ("ORD-00607", "Blender", "Khulna", 8, 123.69, 0.0)
]


def get_revenue(order):
    return round(order[3] * order[4] * (1 - order[5]), 2)


def sales_summary(revenues):
    return round(sum(revenues), 2), min(revenues), max(revenues)


print("\n1. Fixed Business Configuration")
print("These tuples store approved business categories, regions and discount rates.")

print("Available categories:", CATEGORIES)
print("Approved regions:", REGIONS)
print("Allowed discounts:", DISCOUNT_RATES)
print("Is Sylhet an approved region?", "Sylhet" in REGIONS)


print("\n2. Protecting Business Configuration")
print("Business configuration should not change accidentally during program execution.")

try:
    REGIONS[0] = "New Region"
except TypeError:
    print("Protection successful: Region configuration cannot be modified.")

print("Original regions:", REGIONS)


print("\n3. Sales Record Unpacking")
print("Extracting individual details from a fixed sales record.")

order_id, product, region, units, price, discount = orders[0]

print(f"Order ID: {order_id}")
print(f"Product: {product}")
print(f"Region: {region}")
print(f"Quantity: {units} units")
print(f"Discount: {discount:.0%}")


print("\n4. Regional Sales Summary")
print("Counting orders and revenue for each approved sales region.")

for region_name in REGIONS:
    regional_orders = [order for order in orders if order[2] == region_name]
    regional_revenue = sum(get_revenue(order) for order in regional_orders)

    if regional_orders:
        print(f"{region_name}: {len(regional_orders)} orders | "
              f"{regional_revenue:,.2f} BDT")


print("\n5. Sales Statistics Using a Tuple")
print("Returning total, lowest and highest order revenue together.")

revenues = [get_revenue(order) for order in orders]

total, lowest, highest = sales_summary(revenues)

print(f"Total revenue: {total:,.2f} BDT")
print(f"Lowest order: {lowest:,.2f} BDT")
print(f"Highest order: {highest:,.2f} BDT")


print("\n6. Business Menu")
print("Displaying fixed menu options using a tuple.")

MENU = ("Sales Report", "Product Analysis", "Demand Forecast", "Inventory Report")

for number, option in enumerate(MENU, start=1):
    print(f"{number}. {option}")


print("\n7. Regional Sales Lookup")
print("Enter an approved region to view its sales performance.")

selected_region = input("Enter region name: ").strip().title()

if selected_region in REGIONS:
    matching_orders = [order for order in orders if order[2] == selected_region]
    revenue = sum(get_revenue(order) for order in matching_orders)
    units_sold = sum(order[3] for order in matching_orders)

    print(f"\nRegion: {selected_region}")
    print(f"Total orders: {len(matching_orders)}")
    print(f"Units sold: {units_sold}")
    print(f"Total revenue: {revenue:,.2f} BDT")
else:
    print("Invalid region. Please select an approved sales region.")
