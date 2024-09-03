#Task 1: Write a function that lets the user add items to a list.
#Task 2: Include a function to remove items from the list.
#Task 3: Add a function that prints out the entire list in a formatted way.

the_list = []

def add_item():
    item = input("Enter item to add to shopping list: ")
    the_list.append(item)

def remove_item():
    item = input("Enter the item to remove from shopping list: ")
    if item in the_list:
        the_list.remove(item)
    else:
        print("Item not found.")

def show():
    if the_list:
        print("Your list:")
        for i, item in enumerate(the_list, start=1):
            print(f"{i}. {item}")
    else:
        print("Your list is empty.")

while True:
    print("\nOptions: add, remove, show, exit")
    choice = input("Choose an option: ").strip().lower()

    if choice == "add":
        add_item()
    elif choice == "remove":
        remove_item()
    elif choice == "show":
        show()
    elif choice == "exit":
        print("Exiting...")
        break
    else:
        print("Invalid option, try again.")