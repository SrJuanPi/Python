# Facilitating money management when shopping in supermarkets

# We ask for spending money
# In case of not entering a number, we handle an exception.
while True:
    try: available_money = float(input("Enter the money you have to spend: "))
    except: print("Enter a number")
    else: break

shopping_list = [] # Final shopping list with all the details.

# Adding prices as they are added
def add_prices(shopping_list):
    total = 0
    for product in shopping_list:
        total += product['price'] * product['quantity']
    return total

# Function to remove a product by name
def remove_product(shopping_list, product_name):
    for product in shopping_list:
        if product['product'].lower() == product_name.lower():
            shopping_list.remove(product)
            return True
    return False

# Add as many products as the user requires.
while True:
    
    action = input("Enter 'add' to add a product, 'remove' to remove a product, or 'exit' to continue: ").lower()
    if action == "exit": break
    elif action == "add":
        product = input("Enter product: ")
        while True:  # Exception handling
            try: price = float(input("Unit price: "))
            except: print("Enter a number")
            else: break
        while True:
            try: quantity = int(input("Number of units: "))
            except: print("Enter a number")
            else: break

        # Product data is added to the list
        shopping_list.append({'product': product, 'price': price, 'quantity': quantity})
        # The prices are added as they are added to keep count
        print(f"Total Price: {add_prices(shopping_list)}")
    elif action == "remove":
        product_name = input("Enter the name of the product to remove: ")
        if remove_product(shopping_list, product_name): print(f"{product_name} has been removed.")
        else: print(f"{product_name} not found in the shopping list.")

# We show the complete shopping_list of products with their details.
for product in shopping_list:
    print(f"\nProduct: {product['product']}\nPrice: {product['price']}\nQuantity: {product['quantity']}")

# We verify whether or not the user can pay for the purchase.
if add_prices(shopping_list) <= available_money:
    print(f"\nTotal price is: {add_prices(shopping_list)} and you have {abs(available_money - add_prices(shopping_list))} left over.")

else: print(f"\nYou can't afford it, you're {abs(available_money - add_prices(shopping_list))} short.")




# Successfully completed!