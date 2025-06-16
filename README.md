## 🧾 Product Inventory Manager

A Python CLI tool to manage inventory from a CSV file.
It helped me practice file handling, data processing, and clean output formatting — essential for building real-world backend tools.

⸻

## 🎯 Why I Built This

At this point in my learning, I wanted to move beyond CLI logic and try working with external files and structured data.
This was the first time I loaded .csv data into memory, applied calculations, and displayed it with formatting.

⸻

## ✨ Features
- Load product data from products.csv
- Display all products with clean, aligned output
- Search products by name (case-insensitive)
- Calculate total inventory value (price × quantity)

## 🧠 Tech & Concepts
- Python OOP (classes, instance methods, attribute access)
- File I/O with the csv module
- String formatting for clean CLI output
- Basic error handling and data validation

## 📁File Structure

```
product_manager/
├── main.py              # Entry point of the program
├── product.py           # Product class
├── inventory.py         # Inventory logic
├── products.csv         # Sample product data
└── README.md            # Project description
```

## ▶️How to Run

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

## 👩‍💻 Author

Created by Kateryna Babakova (https://github.com/katebabakova444)
This project is part of my backend development journey.
View my full portfolio: kateryna-portfolio (https://github.com/katebabakova444/kateryna-portfolio)