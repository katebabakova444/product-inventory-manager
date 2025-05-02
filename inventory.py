import csv
from product import Product
class Inventory:
    def __init__(self, csv_file):
        self.products = []
        self.load_products(csv_file)
    def load_products(self, csv_file):
        with open(csv_file, newline='', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                product = Product(
                    row['Name'],
                    row['Category'],
                    row['Price'],
                    row['Quantity']
                )
                self.products.append(product)
    def list_all(self):
        return self.products

    def find_by_name(self, name):
        return [p for p in self.products if name.lower() in p.name.lower()]

    def total_inventory_value(self):
        return sum(p.total_value() for p in self.products)

