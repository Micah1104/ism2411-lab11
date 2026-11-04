#exercise 1 
print("--Exercise 1--")
customer = {
    "name": "Alice",
    "email": "alice@example.com",
    "tier": "gold",
    "ytd_spend": 12400,
}
print(customer["name"])
print(customer["email"])
print(customer["tier"])
print(customer["ytd_spend"])

print("--Exercise 2--")

customer["phone"]= "555-5555" #add new key/value
print(customer)
customer["tier"]= "platinum"
print(customer)
del customer["email"]
print(customer)

print("--Exercise 3--")
print(customer.get("email", 'no email on file'))

# try:
#     print(customer["email"])
# except KeyError as error:
#     print("KeyError caught:", error)

print("--Exercise 4--")
for key, value in customer.items():
    print(f"{key}: {value}")

for key in customer:
    print(key)

#.items() prints both key and value as just customer prints just the key

print("--Exercise 5--")
tier_discounts = {
    "bronze": 0, 
    "silver": 0.05, 
    "gold": 0.10, 
    "platinum": 0.15
}

purchase = 200
discount_rate = tier_discounts.get(customer["tier"], 0)
final_price = purchase * (1 - discount_rate)
print(f"tier: {customer['tier']}")
print(f"discount rate: {discount_rate * 100}%")
print(f"final price: ${final_price:.2f}")

print("--Exercise 6--")

customers = [
    {"name": "Bob", "tier": "silver", "ytd_spend": 3200},
    {"name": "Carol", "tier": "gold", "ytd_spend": 8750},
    {"name": "David", "tier": "bronze", "ytd_spend": 450},
]

for record in customers:
    rate = tier_discounts.get(record["tier"], 0)
    discount = 300 * rate
    print(f"{record['name']} ({record['tier']}): ${discount:.2f} off a $300 purchase")

print("--Exercise 7--")

catalog = {
    "Widget A": {"price": 9.99, "stock": 150},
    "Gadget C": {"price": 49.99, "stock": 8}
}

for name, details in catalog.items():
    if details["stock"] < 20:
        print(f"LOW STOCK: {name} - only {details['stock']} left")

print("--Exercise 8--")
transactions = [
    {"region": "north", "amount": 150},
    {"region": "south", "amount": 300},
]

sale_by_region = {}
for sale in transactions:
    region = sale["region"]
    amount = sale["amount"]
    sale_by_region[region] = sale_by_region.get(region, 0) + amount

print(sale_by_region)

for region in sorted(sale_by_region):
    print(f"{region}: ${sale_by_region[region]:.2f}")
    