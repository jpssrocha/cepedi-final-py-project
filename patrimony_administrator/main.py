"""
Entry point for this patrimony administrator.
"""
from .patrimony_io_manager import PatrimonyIOManager

def show_all_itens():
    """
    Show all patrimony items in a condensed view. Only the most relevant
    information.
    """
    pass


def show_balance_sheet():
    """Show a balance sheet from the patrimony items"""
    pass


def show_net_and_value():
    """Show aggregated net flow and value of patrimony items"""
    pass


def create_item():
    """Create a new patrimony item"""
    pass


def read_item(item_id):
    """Read all info from patrimony item"""
    pass


def update_item(item_id):
    """Update patrimony item properties"""
    pass


def delete_item(item_id):
    """Delete patrimony item"""
    pass


def main():
    """Balance administrator interface"""

    print(
        """
        Balance Administrator
        ---------------------

        Select option:

            0. Exit program
            1. See all items
            2. See balance sheet
            3. See net flow and patrimony value
            4. Create patrimony item
            5. Read patrimony item
            6. Update item
            7. Delete patrimony item
        """
    )

    on = True

    while on:

        option = input("Option: ")

        if option == "1":
            print("Triggering code to show all items (to implement)")

        elif option == "2":
            print("Triggering code to show balance sheet (to implement)")

        elif option == "3":
            print("Triggering code to show new flow and total value (to implement)")

        elif option == "4":
            print("Triggering code to add item (to implement)")

        elif option == "5":
            print("Triggering code to update item (to implement)")

        elif option == "6":
            print("Triggering code to subtract item (to implement)")

        elif option == "0":
            print("Exiting program ...")
            on = False

        else:
            print("Invalid option!")


if __name__ == "__main__":
    main()

