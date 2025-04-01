from Grocery import Grocery

class GroceryStore:
    
    def __init__(self):

        self.inventory = {
            "pizza": Grocery("Pizza", 4.50),
            "milk": Grocery("Milk", 1.50),
            "bread": Grocery("Bread", 0.80),
            "cereal": Grocery("Cereal", 2.10)
        }
        

        self.cart = {}

    def display_inventory(self):
        """Displays available groceries and their prices."""
        print("\nAvailable Groceries and Prices:")
        for grocery in self.inventory.values():
            print(f"{grocery.name}: ${grocery.price:.2f}")

    def add_to_cart(self):
        """Allows the user to add groceries to their cart."""
        self.display_inventory()
        
        grocery_name = input("\nEnter the grocery name you want to add: ").strip().lower()

        if grocery_name not in self.inventory:
            print("This grocery item is not available. Please choose from the list.")
            return
        
        try:
            quantity = int(input(f"How many of {self.inventory[grocery_name].name} would you like? "))
            if quantity <= 0:
                print("Invalid quantity! Defaulting to 1.")
                quantity = 1
        except ValueError:
            print("Invalid input! Defaulting to 1.")
            quantity = 1

        if grocery_name in self.cart:
            self.cart[grocery_name] += quantity
        else:
            self.cart[grocery_name] = quantity
            
        print(f"Added {quantity} {self.inventory[grocery_name].name}(s) to your cart.")

    def calculate_total(self):
        """Calculates the total cost of all items in the cart."""
        if not self.cart:
            print("Your cart is empty.")
            return

        total_cost = 0
        print("\nYour Cart:")
        for grocery_name, quantity in self.cart.items():
            grocery = self.inventory[grocery_name]
            item_total = grocery.price * quantity
            print(f"{grocery.name}: {quantity} x ${grocery.price:.2f} = ${item_total:.2f}")
            total_cost += item_total
        
        print(f"\nTotal Price: ${total_cost:.2f}")

    def run(self):
        """Main loop for user interaction."""
        while True:
            print("\nWelcome to the Grocery Store!")
            print("1. View Groceries")
            print("2. Add to Cart")
            print("3. View Cart and Total Price")
            print("4. Exit")
            
            choice = input("Enter your choice: ").strip()

            if choice == "1":
                self.display_inventory()
            elif choice == "2":
                self.add_to_cart()
            elif choice == "3":
                self.calculate_total()
            elif choice == "4":
                print("Thank you for shopping with us!")
                break
            else:
                print("Invalid choice! Please select a valid option.")


if __name__ == "__main__":
    store = GroceryStore()
    store.run()
