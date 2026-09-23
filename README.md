Shopping Cart

A simple terminal-based Shopping Cart program built with Python.

This program allows users to view available products, add products to a shopping cart, enter quantities, combine repeated products, view the cart, calculate discounts, and checkout with a final invoice.

Features

Display available products

Add products to cart

Enter product quantity

Validate product number

Validate quantity

Prevent zero or negative quantities

Combine repeated products

View cart

Calculate cart total

Apply automatic discount

Print final invoice

Checkout order

Quit without buying

Handle empty cart

Products
No.	Product	Price
1	T-Shirt	Rs. 800
2	Jeans	Rs. 1800
3	Shoes	Rs. 2500
4	Cap	Rs. 300
5	Jacket	Rs. 3200
6	Socks	Rs. 150
Program Options

After displaying the products, the program provides four options:

a. Add item to cart
b. View cart
c. Checkout
d. Quit without buying

Option A - Add Item to Cart

The user can select a product by entering its product number.

Example:

Enter product number to add: 1
Enter quantity for T-Shirt: 2

Added 2 x T-Shirt to your cart.


The selected product is added to the cart with the entered quantity.

Option B - View Cart

The user can view all products currently in the cart.

Example:

--- Your Cart ---
Item           Qty  Price     Total
----------------------------------------
T-Shirt        2    800       1600
Jeans          1    1800      1800
----------------------------------------
Cart Total: Rs. 3400


The program calculates the total price of each item using:

Item Total = Quantity × Price


The cart total is the sum of all item totals.

Option C - Checkout

When the user selects checkout, the program calculates the total amount and applies the appropriate discount.

Discount Rules
Cart Total	Discount
Rs. 2000 or less	0%
Above Rs. 2000	5%
Above Rs. 5000	10%

The discount is calculated before the final total.

Bill Calculation
Discount Amount = Total × Discount Percentage / 100

Grand Total = Total - Discount Amount


For example, if the cart total is Rs. 3400:

Discount = 3400 × 5 / 100
Discount = Rs. 170

Grand Total = 3400 - 170
Grand Total = Rs. 3230

Checkout Invoice

A final invoice is displayed during checkout.

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

Repeated Products

If the same product is added more than once, the program combines its quantity instead of adding a duplicate product.

For example:

T-Shirt × 2
T-Shirt × 3


will be stored as:

T-Shirt × 5


The product appears only once in the cart.

Input Validation

The program validates the product number before adding an item.

If the user enters an invalid product number:

Enter product number to add: 9

Invalid product number.


The program also checks that the quantity is greater than zero.

Example:

Enter quantity for T-Shirt: 0

Quantity must be greater than 0.


Negative quantities are also rejected.

Empty Cart

If the user selects View Cart without adding any products, the program displays:

Your cart is empty.


If the user selects Checkout without adding any products, the program displays:

Your cart is empty. Nothing to checkout.


The program then returns to the main menu.

Quit Without Buying

The user can select option d to exit without completing a purchase.

Example:

Exiting without purchase. Goodbye!


The program then ends.

Python Concepts Used

This project practices several basic Python concepts:

Functions

Lists

Tuples

if, elif, and else

for loops

while loops

break

continue

User input with input()

Input validation

int()

isdigit()

len()

range()

List indexing

append()

Boolean variables

Arithmetic operations

Percentage calculations

f-strings

How the Program Works

The program creates a list of products and their prices.

An empty cart is created.

The product menu is displayed.

The user selects an option.

If the user chooses a, a product is added to the cart.

The program validates the product number.

The user enters a quantity.

The program validates the quantity.

If the product already exists, its quantity is increased.

If the product does not exist, it is added to the cart.

The user can view the cart using option b.

The user can checkout using option c.

The subtotal is calculated.

The appropriate discount is applied.

The final invoice is displayed.

The user can quit without buying using option d.

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

Save the Python code in a file named:

shopping_cart.py

3. Run the Program

Open a terminal in the project directory and run:

python shopping_cart.py

Example

A typical program flow looks like this:

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


The user can continue adding products, view the cart, and finally choose checkout.

Possible Improvements

Future versions could include:

Remove products from cart

Update product quantities

Customer name

Customer contact information

Order number

Date and time

Payment method

Save invoice to a file

More products

Product categories

Tax calculation

Stock management

Database integration

Graphical user interface

Unit testing

Purpose

This project is created for Python practice and learning.

It helps beginners understand how lists, tuples, loops, conditions, functions, input validation, calculations, and user input can be combined to create a practical terminal-based shopping cart application.

License

This project is intended for educational and practice purposes.