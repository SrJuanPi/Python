# Program that calculates the Profitability of a Product

def calculate_profitability():
    print("Is this product profitable for me?")
    print("Profitability scale: x/25 — final value as a percentage %\n")

    # Product data
    capital = float(input("Enter your available capital in USD: "))
    price = float(input("Enter the product price in USD: "))
    score = 0

    durability = int(input("""
Durability options:

1) 1 month or less
2) more than 1 month and less than 6 months
3) more than 6 months and less than 1 year
4) more than 1 year and less than 3 years
5) 3 years or more

Select (1-5): """))

    offer = int(input("""
Product offer compared to alternatives:

1) Offers less than other alternatives
2) Offers a little less than other alternatives
3) Offers the same as other alternatives
4) Offers a little more than other alternatives
5) Offers more than other alternatives

Select (1-5): """))

    location = int(input("""
Where the product can be purchased:

1) Mini market or supermarket
2) Shopping center
3) International purchase
4) Online store
5) Dedicated shop

Select (1-5): """))

    need = int(input("""
Do you really need this product?

1) I don't need this product
2) Occasional use
3) Useful but can live without it
4) Useful for me
5) Basic necessity

Select (1-5): """))

    # Price/Capital score
    if price < (capital * 0.2):
        score = 5
    elif price < (capital * 0.5):
        score = 4
    elif price == (capital * 0.5):
        score = 3
    elif price < (capital * 0.8):
        score = 2
    elif price < capital:
        score = 1
        print("Not worth it — you'll be left with little money.")
    elif price > capital:
        print("NOT WORTH IT — YOU WILL END UP IN DEBT.")
    else:
        print("Invalid value, please enter a numeric value.")

    # Add scores for the other categories (validate 1-5)
    if 1 <= durability <= 5:
        score += durability
    else:
        print("Invalid durability value, please enter a number 1-5.")

    if 1 <= offer <= 5:
        score += offer
    else:
        print("Invalid offer value, please enter a number 1-5.")

    if 1 <= location <= 5:
        score += location
    else:
        print("Invalid location value, please enter a number 1-5.")

    if 1 <= need <= 5:
        score += need
    else:
        print("Invalid need value, please enter a number 1-5.")

    # Calculate percentage (max score = 25)
    profitability_percent = (score / 25) * 100
    print(f"The product profitability is: {round(profitability_percent, 2)}%")

if __name__ == "__main__":
    calculate_profitability()