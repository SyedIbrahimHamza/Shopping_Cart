def shopping_cart():
    products = [
        ("T-Shirt", 800),
        ("Jeans", 1800),
        ("Shoes", 2500),
        ("Cap", 300),
        ("Jacket", 3200),
        ("Socks", 150),
    ]
    cart = []
    print("\n--- Welcome to the Shop ---")
    while True:
        print("\nProducts:")
        for i in range(len(products)):
            name, price = products[i]
            print(f"{i + 1}. {name} - Rs. {price}")
        print("\n--- Options ---")
        print("a. Add item to cart")
        print("b. View cart")
        print("c. Checkout")
        print("d. Quit without buying")
        choice = input("Choose an option (a/b/c/d): ").lower() 
        if choice == 'a':
            item_choice = input("Enter product number to add: ")

            if not item_choice.isdigit() or not (1 <= int(item_choice) <= len(products)):
                print("Invalid product number.")
                continue

            index = int(item_choice) - 1
            name, price = products[index]

            qty = int(input(f"Enter quantity for {name}: "))
            if qty <= 0:
                print("Quantity must be greater than 0.")
                continue

            found = False
            for entry in cart:
                if entry[0] == name:
                    entry[1] += qty
                    found = True
                    break

            if not found:
                cart.append([name, qty, price])

            print(f"Added {qty} x {name} to your cart.")
        elif choice == 'b':
            if not cart:
                print("\nYour cart is empty.")
            else:
                print("\n--- Your Cart ---")
                print(f"{'Item':<15}{'Qty':<5}{'Price':<10}{'Total':<10}")
                print("-" * 40)
                cart_total = 0
                for name, qty, price in cart:
                    item_total = qty * price
                    cart_total += item_total
                    print(f"{name:<15}{qty:<5}{price:<10}{item_total:<10}")
                print("-" * 40)
                print(f"Cart Total: Rs. {cart_total}")
        elif choice == 'c':
            if not cart:
                print("\nYour cart is empty. Nothing to checkout.")
                continue

            total = 0
            for name, qty, price in cart:
                total += qty * price

            discount_percent = 0
            if total > 5000:
                discount_percent = 10
            elif total > 2000:
                discount_percent = 5

            discount_amount = (discount_percent / 100) * total
            grand_total = total - discount_amount

            print("\n========= INVOICE =========")
            print(f"{'Item':<15}{'Qty':<5}{'Price':<10}{'Total':<10}")
            print("-" * 40)
            for name, qty, price in cart:
                item_total = qty * price
                print(f"{name:<15}{qty:<5}{price:<10}{item_total:<10}")
            print("-" * 40)
            print(f"Subtotal: Rs. {total}")
            print(f"Discount ({discount_percent}%): -Rs. {discount_amount:.2f}")
            print(f"Grand Total: Rs. {grand_total:.2f}")
            print("============================")
            print("Thank you for shopping with us!")
            break
        elif choice == 'd':
            print("\nExiting without purchase. Goodbye!")
            break

        else:
            print("\nInvalid option. Please choose a, b, c, or d.")