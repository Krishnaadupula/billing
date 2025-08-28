
# 🛒 Simple Billing System in Python


This is a beginner-friendly command-line billing system built using Python. It allows users to select items from a predefined product list, specify quantities, and view a final bill with total cost.

## 📦 Features

- Displays available products with prices  
- Accepts user input for item selection and quantity  
- Validates input and handles errors gracefully  
- Calculates and displays a formatted final bill  

## 🧠 Prerequisites

- Python 3.x installed  
- Basic understanding of dictionaries and loops in Python  

## 🚀 How It Works

```python
# Product catalog with prices
product = {
    'milk': 30,
    'rice': 50
}

# Display available products
print("Available products:")
for item, price in product.items():
    print(f"{item.capitalize():10} - ₹{price}")

# Initialize empty cart
cart = {}

# Shopping loop
while True:
    item = input("\nEnter the item (or type 'done' to finish): ").lower()
    if item == 'done':
        break
    elif item in product:
        try:
            qty = int(input(f"How many units of {item} do you want? "))
            if qty <= 0:
                print("Quantity must be positive.")
                continue
            cart[item] = cart.get(item, 0) + qty
        except ValueError:
            print("Please enter a valid number.")
    else:
        print("Item not found. Try again.")

# Final bill
print("\n🧾 Final Bill")
total_price = 0
for item, qty in cart.items():
    price = product[item]
    item_total = price * qty
    total_price += item_total
    print(f"{item.capitalize():10} x {qty:<3} = ₹{item_total}")

print(f"\nTotal Amount: ₹{total_price}")
```

## 📌 Sample Output

```
Available products:
Milk       - ₹30
Rice       - ₹50

Enter the item (or type 'done' to finish): milk
How many units of milk do you want? 2

Enter the item (or type 'done' to finish): rice
How many units of rice do you want? 1

Enter the item (or type 'done' to finish): done

🧾 Final Bill
Milk       x 2   = ₹60
Rice       x 1   = ₹50

Total Amount: ₹110
```

## 🛠️ Customization Ideas

- Add stock limits or inventory tracking  
- Include discounts or tax calculations  
- Save bills to a file or database  
- Build a GUI using Tkinter or PyQt  

## 📚 License

This project is open-source and free to use for educational purposes.
