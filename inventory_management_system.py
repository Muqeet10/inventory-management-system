# Inventory Management System in Python

inventory = {}

def add_item():
    item = input("Enter item name to add: ").strip()
    if item in inventory:
        print(f"Item '{item}' already exists. Use update option to change quantity.")
        return
    try:
        quantity = int(input("Enter quantity: "))
        inventory[item] = quantity
        print(f"Item '{item}' added with quantity {quantity}.")
    except ValueError:
        print("Please enter a valid number for quantity.")

def update_item():
    item = input("Enter item name to update: ").strip()
    if item in inventory:
        try:
            quantity = int(input("Enter new quantity: "))
            inventory[item] = quantity
            print(f"Item '{item}' updated to quantity {quantity}.")
        except ValueError:
            print("Invalid quantity.")
    else:
        print(f"Item '{item}' not found.")

def remove_item():
    item = input("Enter item name to remove: ").strip()
    if item in inventory:
        del inventory[item]
        print(f"Item '{item}' removed.")
    else:
        print(f"Item '{item}' not found.")

def view_inventory():
    if not inventory:
        print("Inventory is empty.")
    else:
        print("\nCurrent Inventory:")
        for item, qty in inventory.items():
            print(f" - {item}: {qty}")
        print()

def main():
    while True:
        print("\nInventory Management System")
        print("1. Add Item")
        print("2. Update Item")
        print("3. Remove Item")
        print("4. View Inventory")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            add_item()
        elif choice == '2':
            update_item()
        elif choice == '3':
            remove_item()
        elif choice == '4':
            view_inventory()
        elif choice == '5':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please enter a number between 1-5.")

if __name__ == "__main__":
    main()
