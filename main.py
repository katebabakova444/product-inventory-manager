from inventory import Inventory

inventory = Inventory("products.csv")

print("All products: ")
for product in inventory.list_all():
    print(product)

print("\nSearch for 'Mouse'; ")
results = inventory.find_by_name("Mouse")
for product in results:
    print(product)
print("\nTotal inventory value: ")
print(f"${inventory.total_inventory_value():.2f}")