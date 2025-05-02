# Product Inventory Manager

This is a simple Python console application that manages a product inventory loaded from a CSV file.  
It demonstrates basic object-oriented programming, file handling, and data processing.

## Features

- Load product data from `products.csv`
- Display all products with formatted output
- Search for products by name (case-insensitive)
- Calculate total value of all items in inventory (price × quantity)

## Technologies

- Python 3
- Standard Library: `csv`

## File Structure

```
product_manager/
├── main.py              # Entry point of the program
├── product.py           # Product class
├── inventory.py         # Inventory logic
├── products.csv         # Sample product data
└── README.md            # Project description
```

## How to Run

1. Make sure you have Python 3 installed.
2. Place the `products.csv` file in the same directory as the Python files.
3. Run the app:

```bash
python main.py
```

## Example Output


```
All products:
Laptop (Electronics) - $999.99 × 10 pcs
Phone (Electronics) - $599.99 × 25 pcs
...

Search for 'Mouse':
Mouse (Accessories) - $29.99 × 40 pcs

Total inventory value:
$2949.25
```

## Author

Kateryna Babakova