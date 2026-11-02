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
print(customer.get("email", 'not found'))