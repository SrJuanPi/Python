"""
Shopping Cart System Module.

A simple shopping cart management system with inventory tracking,
discount calculation, and receipt generation.
"""

from typing import List, Dict, Optional
from utils import get_valid_input


class ShoppingCart:
    """Manages shopping cart operations."""
    
    def __init__(self) -> None:
        """Initialize an empty shopping cart."""
        self.items: List[Dict[str, any]] = []
        self.tax_rate: float = 0.08
    
    def add_item(self, name: str, price: float, quantity: int = 1) -> bool:
        """
        Add an item to the cart.
        
        Args:
            name: Product name
            price: Product price
            quantity: Quantity to add
            
        Returns:
            True if successful, False otherwise
        """
        if price < 0 or quantity < 1:
            print("Error: Price must be positive and quantity must be at least 1")
            return False
        
        existing_item = next((item for item in self.items if item['name'] == name), None)
        
        if existing_item:
            existing_item['quantity'] += quantity
        else:
            self.items.append({
                'name': name,
                'price': price,
                'quantity': quantity
            })
        
        print(f"Added {quantity} x {name} to cart")
        return True
    
    def remove_item(self, name: str) -> bool:
        """
        Remove an item from the cart.
        
        Args:
            name: Product name to remove
            
        Returns:
            True if removed, False if not found
        """
        initial_length = len(self.items)
        self.items = [item for item in self.items if item['name'] != name]
        
        if len(self.items) < initial_length:
            print(f"Removed {name} from cart")
            return True
        
        print(f"Item '{name}' not found in cart")
        return False
    
    def calculate_subtotal(self) -> float:
        """Calculate subtotal before tax."""
        return sum(item['price'] * item['quantity'] for item in self.items)
    
    def calculate_tax(self) -> float:
        """Calculate tax amount."""
        return self.calculate_subtotal() * self.tax_rate
    
    def calculate_total(self) -> float:
        """Calculate total with tax."""
        return self.calculate_subtotal() + self.calculate_tax()
    
    def apply_discount(self, discount_percent: float) -> float:
        """
        Apply a discount to the cart.
        
        Args:
            discount_percent: Discount percentage (0-100)
            
        Returns:
            Discount amount
        """
        if discount_percent < 0 or discount_percent > 100:
            print("Error: Discount must be between 0 and 100")
            return 0
        
        discount = self.calculate_subtotal() * (discount_percent / 100)
        return discount
    
    def display_cart(self) -> None:
        """Display current cart contents."""
        if not self.items:
            print("\nCart is empty\n")
            return
        
        print("\n--- Shopping Cart ---")
        print(f"{'Item':<20} {'Price':>10} {'Qty':>5} {'Total':>10}")
        print("-" * 45)
        
        for item in self.items:
            total = item['price'] * item['quantity']
            print(f"{item['name']:<20} ${item['price']:>9.2f} {item['quantity']:>5} ${total:>9.2f}")
        
        print("-" * 45)
        print(f"{'Subtotal:':<35} ${self.calculate_subtotal():>9.2f}")
        print(f"{'Tax (8%):':<35} ${self.calculate_tax():>9.2f}")
        print(f"{'TOTAL:':<35} ${self.calculate_total():>9.2f}\n")
    
    def clear_cart(self) -> None:
        """Clear all items from cart."""
        self.items.clear()
        print("Cart cleared\n")


def main() -> None:
    """Main function to run the shopping cart system."""
    cart = ShoppingCart()
    
    print("=== Shopping Cart System ===\n")
    
    while True:
        print("Menu:")
        print("1. Add item")
        print("2. Remove item")
        print("3. View cart")
        print("4. Apply discount")
        print("5. Checkout")
        print("6. Clear cart")
        print("7. Exit")
        
        choice = input("\nSelect an option (1-7): ").strip()
        
        if choice == '1':
            name = input("Item name: ").strip()
            price = get_valid_input("Price: $", float)
            if price is not None and price > 0:
                quantity = get_valid_input("Quantity: ", int)
                if quantity is not None and quantity > 0:
                    cart.add_item(name, price, quantity)
        
        elif choice == '2':
            cart.display_cart()
            name = input("Item name to remove: ").strip()
            cart.remove_item(name)
        
        elif choice == '3':
            cart.display_cart()
        
        elif choice == '4':
            discount_percent = get_valid_input("Discount percentage: ", float)
            if discount_percent is not None:
                discount = cart.apply_discount(discount_percent)
                print(f"Discount applied: ${discount:.2f}\n")
        
        elif choice == '5':
            cart.display_cart()
            print("Thank you for your purchase!")
            cart.clear_cart()
        
        elif choice == '6':
            cart.clear_cart()
        
        elif choice == '7':
            print("Goodbye!")
            break
        
        else:
            print("Invalid option. Please try again.\n")


if __name__ == "__main__":
    main()