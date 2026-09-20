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