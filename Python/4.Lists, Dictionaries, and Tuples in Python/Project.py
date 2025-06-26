# Inventory Manager Program
# Step 1: Create the inventory
inventory = {
    "pen":(30,5.0),
    "notebook":(15,20.0)
}
# Display inventory
print("\n Current inventory")
for i, (q,p) in inventory.items():
    print(f"Item: {i}, Quantity: {q}, Price: ${p}")
total=sum(q*p for q,p in inventory.values())
print(f"Total value of inventory: ${total:2f}")

# Step 2: Add,Remove, Update Items
i=input("Enter item name to add: ").lower()
q = int(input(f"Enter quantity of {i}: "))
p = float(input(f"Enter price of {i}: "))
inventory[i] = (q, p)
print(f"{i.capitalize()} added successfully!")

i = input("Enter item name to remove: ").lower()
if i in inventory:
    del inventory[i]
    print(f"{i.capitalize()} removed from inventory.")
else:
    print("Item not found.")

i = input("Enter item name to update: ").lower()
if i in inventory:
    q = int(input("Enter new quantity: "))
    p = float(input("Enter new price: "))
    inventory[i] = (q, p)
    print(f"{i.capitalize()} updated successfully!")
else:
    print("Item not found.")

print("\nUpdated Inventory:")
for i, (q,p) in inventory.items():
    print(f"Item: {i}, Quantity: {q}, Price: ${p}")
total=sum(q*p for q,p in inventory.values())
print(f"Total value of inventory: ${total:.2f}")
