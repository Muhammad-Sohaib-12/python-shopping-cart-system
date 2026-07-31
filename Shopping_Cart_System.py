import random

# -------------------------- STORE DATA --------------------------
store = {
    "Fruits": {
        "Apples": 3, "Oranges": 2, "Peach": 6.9, "Mangoes": 5,
        "Bananas": 2, "Papaya": 5, "Strawberry": 1, "Grapefruits": 7
    },
    "Snacks": {
        "Lays": 3, "Cheetos": 3, "Kurkure": 3, "Doritos": 5,
        "Pringles": 8, "Cupcakes": 2, "GALA Biscuit": 6.9,
        "Sooper Biscuit": 3, "Prince Biscuit": 3, "Rio": 3,
        "DairyMilk": 4, "Perk": 2, "Mars": 5, "Snickers": 5, "Kitkat": 3.9
    },
    "Drinks": {
        "CocaCola": 2, "Sprite": 2, "Fanta": 2, "String": 6.9,
        "Redbull": 5, "Mineral Water": 1, "Tang": 1.5,
        "Slice Juice": 1, "Whiskey": 16.9, "Vodka": 14.9,
        "Tequila": 18.23, "Beer": 10, "Red Wine": 20,
        "White Wine": 17.5, "Champagne": 23
    },
    "Household": {
        "Shampoo": 5, "Soap": 3, "Handwash": 3, "Surf": 5,
        "Bleach": 2, "Tissue": 2, "Garbage bags": 0.5,
        "Toothbrush": 2, "Toothpaste": 3, "Air Freshners": 4
    },
    "Vegetables": {
        "Cucumber": 0.69, "Potato": 1, "Tomato": 1, "Onion": 1,
        "Eggplant": 1, "LadyFinger": 1, "Carrot": 1,
        "Garlic": 1, "Ginger": 1, "Lettuce": 1
    },
    "Electronics": {
        "Electric kettle": 25, "Toaster": 20, "Sandwich Maker": 27,
        "Coffee Maker": 25, "Hair Dryer": 23, "Ceiling Fan": 33,
        "LED Bulb": 12, "Headphones": 17, "Power Bank": 24
    }
}

# ---------------- ADMIN LOGIN ----------------
ADMIN_USERNAME = "admin"
ADMIN_PASSWORD = "1234"


# ---------------- DISCOUNT SYSTEM ----------------
def generate_discounts():
    discounts = {}
    for category in store:
        discounts[category] = {}
        for item in store[category]:
            discounts[category][item] = random.choice([0, 5, 10, 15, 20])
    return discounts


# ---------------- SHOW STORE (FORMATTED) ----------------
def show_store(discounts, category=None):
    if category:
        print(f"\n--- {category} ---")
        for item in store[category]:
            price = store[category][item]
            discount = discounts[category][item]
            final_price = price - (price * discount / 100)
            print(f"{item:<20} | ${price:<6} | Discount: {discount:>2}% | Final: ${final_price:.2f}")
        print("===========================")

    else:
        print("\n======= STORE ITEMS =======")
        for cat in store:
            print(f"\n--- {cat} ---")
            for item in store[cat]:
                price = store[cat][item]
                discount = discounts[cat][item]
                final_price = price - (price * discount / 100)
                print(f"{item:<20} | ${price:<6} | Discount: {discount:>2}% | Final: ${final_price:.2f}")
        print("===========================")


# ---------------- SHOW CART ----------------
def show_cart(cart):
    print("\n========= YOUR CART =========")
    if not cart:
        print("Your cart is empty.")
        return 0

    total = 0
    for item, price, category in cart:
        print(f"{item:<15} | ${price:.2f} | {category}")
        total += price

    print("Total Price:", round(total, 2))
    return total


# ---------------- PAYMENT SYSTEM ----------------
def process_payment(total_amount):
    while True:
        method = input("Payment method (Card/Cash): ").lower()
        if method == "card":
            print("Payment successful!")
            break
        elif method == "cash":
            cash = float(input("Enter cash amount: "))
            if cash >= total_amount:
                print(f"Change: ${round(cash - total_amount, 2)}")
                break
            else:
                print("Insufficient cash.")
        else:
            print("Invalid method.")

# ---------------- USER SHOPPING ----------------
def shopping_cart_system():
    discounts = generate_discounts()
    cart = []

    while True:
        print("\n========= MAIN MENU =========")
        print("1. View Inventory")
        print("2. Add Item to Cart")
        print("3. Remove Item from Cart")
        print("4. View Cart")
        print("5. Checkout")
        print("6. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            show_store(discounts)

        elif choice == "2":
            while True:
                print("\nCategories:")
                for cat in store:
                    print(cat)

                category = input("Enter category (or back): ")
                if category.lower() == "back":
                    break
                if category not in store:
                    print("Invalid category.")
                    continue

                show_store(discounts, category)

                while True:
                    item = input("Enter item (change / back): ")
                    if item.lower() == "change":
                        break
                    if item.lower() == "back":
                        break
                    if item not in store[category]:
                        print("Item not found.")
                        continue

                    price = store[category][item]
                    discount = discounts[category][item]
                    final_price = price - (price * discount / 100)
                    cart.append((item, final_price, category))
                    print(item, "added to cart.")

                if item.lower() == "back":
                    break

        elif choice == "3":
            if not cart:
                print("Cart is empty.")
                continue

            show_cart(cart)
            name = input("Enter item name to remove: ")
            for i in cart:
                if i[0] == name:
                    cart.remove(i)
                    print("Item removed.")
                    break
            else:
                print("Item not in cart.")

        elif choice == "4":
            show_cart(cart)

        elif choice == "5":
            total = show_cart(cart)
            if total > 0:
                process_payment(total)
                print("Thank you for shopping!")
                break

        elif choice == "6":
            print("Goodbye!")
            break

        else:
            print("Invalid choice.")


# ---------------- ADMIN PANEL ----------------
def admin_panel():
    while True:
        print("\n========= ADMIN MENU =========")
        print("1. Add Item")
        print("2. Remove Item")
        print("3. Change Price")
        print("4. View Store")
        print("5. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            category = input("Category: ")
            if category in store:
                item = input("Item name: ")
                price = float(input("Price: "))
                store[category][item] = price
                print("Item added.")
            else:
                print("Category not found.")

        elif choice == "2":
            category = input("Category: ")
            item = input("Item name: ")
            if category in store and item in store[category]:
                del store[category][item]
                print("Item removed.")
            else:
                print("Item not found.")

        elif choice == "3":
            category = input("Category: ")
            item = input("Item name: ")
            if category in store and item in store[category]:
                store[category][item] = float(input("New price: "))
                print("Price updated.")
            else:
                print("Item not found.")

        elif choice == "4":
            show_store(generate_discounts())

        elif choice == "5":
            break


# ---------------- LOGIN SYSTEM ----------------
def login_system():
    while True:
        print("\n1. Customer")
        print("2. Admin")
        print("3. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            shopping_cart_system()

        elif choice == "2":
            if input("Username: ") == ADMIN_USERNAME and input("Password: ") == ADMIN_PASSWORD:
                admin_panel()
            else:
                print("Wrong credentials.")

        elif choice == "3":
            break

        else :
            print("Invalid choice.")


# ---------------- START PROGRAM ----------------
login_system()