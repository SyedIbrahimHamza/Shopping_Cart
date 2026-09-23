Shopping Cart

A simple terminal-based Shopping Cart application built with Python.

This program allows users to view available products, add products to a shopping cart, enter quantities, combine repeated products, view the cart, apply automatic discounts, and checkout with a final invoice.

Features

Display available products

Add products to cart

Enter product quantity

Validate product number

Validate quantity

Prevent zero and negative quantities

Combine repeated products

View cart

Calculate cart total

Apply automatic discount

Generate final invoice

Checkout the order

Quit without buying

Handle an empty cart

Products
No.	Product	Price
1	T-Shirt	Rs. 800
2	Jeans	Rs. 1800
3	Shoes	Rs. 2500
4	Cap	Rs. 300
5	Jacket	Rs. 3200
6	Socks	Rs. 150
Program Options

The program provides four options:

a. Add item to cart
b. View cart
c. Checkout
d. Quit without buying


The user can select an option by entering a, b, c, or d.

Add Item to Cart

The user can add a product by entering its product number.

Example:

Choose an option (a/b/c/d): a
Enter product number to add: 1
Enter quantity for T-Shirt: 2
Added 2 x T-Shirt to your cart.


The selected product is added to the cart with its quantity and price.

Repeated Products

If the same product is added multiple times, the program combines the quantities.

For example:

T-Shirt × 2
T-Shirt × 3


The cart will contain:

T-Shirt × 5


The same product is displayed only once in the cart.

View Cart

The user can select option b to view the current cart.

Example:

--- Your Cart ---
Item           Qty  Price     Total
----------------------------------------
T-Shirt        2    800       1600
Jeans          1    1800      1800
----------------------------------------
Cart Total: Rs. 3400


The total for each product is calculated as:

Item Total = Quantity × Price


The cart total is the sum of all item totals.

Discount Rules

The program automatically applies a discount during checkout.

Cart Total	Discount
Rs. 2000 or less	0%
Above Rs. 2000	5%
Above Rs. 5000	10%
Discount Calculation
Discount Amount = Total × Discount Percentage / 100


The final amount is calculated as:

Grand Total = Total - Discount Amount

Example

If the cart total is Rs. 3400:

Discount = 3400 × 5 / 100
Discount = Rs. 170

Grand Total = 3400 - 170
Grand Total = Rs. 3230

Checkout

The user can select option c to checkout.

If the cart contains products, the program calculates the subtotal, discount, and grand total.

Example:

========= INVOICE =========
Item           Qty  Price     Total
----------------------------------------
T-Shirt        2    800       1600
Jeans          1    1800      1800
----------------------------------------
Subtotal: Rs. 3400
Discount (5%): -Rs. 170.00
Grand Total: Rs. 3230.00
============================
Thank you for shopping with us!


After displaying the invoice, the program ends.

Empty Cart

If the user selects b without adding any product, the program displays:

Your cart is empty.


If the user selects c without adding any product, the program displays:

Your cart is empty. Nothing to checkout.


The program then returns to the options menu.

Input Validation

The program validates the product number before adding a product.

For example:

Enter product number to add: 9

Invalid product number.


The program also checks that the quantity is greater than zero.

Example:

Enter quantity for T-Shirt: 0

Quantity must be greater than 0.


Negative quantities are also rejected.

Important Note

The current program expects the quantity to be entered as a number. If a non-numeric value such as abc is entered, Python will generate a ValueError.

For example:

Enter quantity for T-Shirt: abc


This behavior is not currently handled by the program.

Quit Without Buying

The user can select option d to exit without completing a purchase.

Example:

Choose an option (a/b/c/d): d

Exiting without purchase. Goodbye!


The program then ends.

How the Program Works

The program creates a list of products and prices.

An empty cart is created.

The product list is displayed.

The available options are displayed.

The user selects an option.

If a is selected, the user chooses a product.

The product number is validated.

The user enters the quantity.

The quantity is checked to make sure it is greater than zero.

If the product already exists in the cart, its quantity is increased.

Otherwise, the product is added to the cart.

If b is selected, the cart contents are displayed.

If c is selected, the subtotal is calculated.

The appropriate discount is calculated.

The final invoice is displayed.

If d is selected, the program exits without purchasing.

Python Concepts Used

This project practices the following Python concepts:

Functions

Lists

Tuples

if, elif, and else

for loops

while loops

break

continue

input()

lower()

isdigit()

int()

len()

range()

List indexing

append()

Boolean variables

Arithmetic operations

Percentage calculations

f-strings

Tuple unpacking

Project Structure
shopping-cart/
│
├── shopping_cart.py
└── README.md

How to Run
1. Install Python

Make sure Python is installed on your computer.

Check the Python version:

python --version

2. Save the Program

Save the Python code as:

shopping_cart.py

3. Run the Program

Open a terminal in the project directory and run:

python shopping_cart.py

Example Program Flow
--- Welcome to the Shop ---

Products:
1. T-Shirt - Rs. 800
2. Jeans - Rs. 1800
3. Shoes - Rs. 2500
4. Cap - Rs. 300
5. Jacket - Rs. 3200
6. Socks - Rs. 150

--- Options ---
a. Add item to cart
b. View cart
c. Checkout
d. Quit without buying

Choose an option (a/b/c/d): a
Enter product number to add: 1
Enter quantity for T-Shirt: 2
Added 2 x T-Shirt to your cart.


The user can continue adding products, view the cart, and checkout when ready.

Possible Improvements

Future versions could include:

Remove products from the cart

Update product quantities

Handle non-numeric quantity input

Add customer name

Add customer contact information

Add order number

Add date and time

Add payment method

Save invoice to a file

Add more products

Add product categories

Add tax calculation

Add stock management

Add database integration

Create a graphical user interface

Add unit testing

Purpose

This project is created for Python practice and learning.

It helps beginners understand how functions, lists, tuples, loops, conditions, input validation, arithmetic operations, and user input can be combined to create a practical terminal-based shopping cart application.

License

This project is intended for educational and practice purposes.