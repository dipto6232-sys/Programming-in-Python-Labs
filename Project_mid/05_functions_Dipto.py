
CURRENCY = "BDT"

def calculate_revenue(units, price, discount=0):
    total = units * price
    return round(total - (total * discount), 2)


def calculate_profit(revenue, units, unit_cost):
    return round(revenue - (units * unit_cost), 2)


def calculate_margin(profit, revenue):
    if revenue == 0:
        return 0
    return round((profit / revenue) * 100, 2)


def show_product_report(product, units, price, unit_cost, discount=0):
    revenue = calculate_revenue(units, price, discount)
    profit = calculate_profit(revenue, units, unit_cost)
    margin = calculate_margin(profit, revenue)

    print(f"\nProduct: {product}")
    print(f"Revenue: {revenue:,.2f} {CURRENCY}")
    print(f"Profit: {profit:,.2f} {CURRENCY}")
    print(f"Profit margin: {margin:.2f}%")


def check_stock(stock, monthly_demand):
    if stock < monthly_demand:
        return "URGENT: Restock immediately!"
    elif stock < monthly_demand * 2:
        return "WARNING: Prepare a restocking order."
    else:
        return "Stock level is sufficient."


print("\n1. Product Financial Analysis")
print("Calculating revenue, profit and profit margin using reusable functions.")

show_product_report("Laptop", 3, 1104.24, 662.04)
show_product_report("Headphones", 1, 144.83, 104.34, 0.10)


print("\n2. Sales Discount Comparison")
print("Comparing revenue with and without a customer discount.")

normal_revenue = calculate_revenue(3, 1104.24)
discounted_revenue = calculate_revenue(3, 1104.24, 0.10)

print(f"Full price revenue: {normal_revenue:,.2f} BDT")
print(f"After 10% discount: {discounted_revenue:,.2f} BDT")


print("\n3. Product Profitability")
print("Checking whether the product generates a healthy profit margin.")

profit = calculate_profit(normal_revenue, 3, 662.04)
margin = calculate_margin(profit, normal_revenue)

if margin < 10:
    print("Low margin: Review product pricing and costs.")
elif margin < 20:
    print("Moderate margin: Monitor profitability.")
else:
    print("Healthy margin: Product is performing well.")

print(f"Current profit margin: {margin:.2f}%")


print("\n4. Inventory Decision")
print("Enter current stock to receive a restocking recommendation.")

stock = int(input("Current Laptop stock: "))
monthly_demand = 427 / 12

print(check_stock(stock, monthly_demand))
