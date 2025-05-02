class Product:
    def __init__(self, name, category, price, quantity):
        self.name = name
        self.category = category
        self.price = float(price)
        self.quantity = int(quantity)
    def total_value(self):
        return self.price * self.quantity
    def __str__(self):
        return(f"{self.name} ({self.category}) - ${self.price:.2f} x {self.quantity} pcs")
