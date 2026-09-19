def shopping_cart():
    products = [
        ("T-Shirt", 800),
        ("Jeans", 1800),
        ("Shoes", 2500),
        ("Cap", 300),
        ("Jacket", 3200),
        ("Socks", 150),
    ]
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