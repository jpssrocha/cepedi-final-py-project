"""
Entry point for this patrimony administrator application
"""
import json
import os

from patrimony_administrator.patrimony_io_manager import PatrimonyIOManager
from patrimony_administrator.patrimony_logic_manager import PatrimonyLogicManager

def show_all_itens(io_manager: PatrimonyIOManager):
    """
    Show all patrimony items in a condensed view. Only the most relevant
    information.
    """
    print()
    print(io_manager)


def show_balance_sheet():
    """Show a balance sheet from the patrimony items"""
    pass


def show_net_and_value():
    """Show aggregated net flow and value of patrimony items"""
    pass


def create_item():
    """Create a new patrimony item"""
    pass


def read_item(io_manager: PatrimonyIOManager):
    """Read all info from patrimony item"""

    id_ = input("Which is the item id number? ")

    print(
        json.dumps(io_manager.read_item(id_), indent=4)
    )


def update_item(item_id):
    """Update patrimony item properties"""
    pass


def delete_item(item_id):
    """Delete patrimony item"""
    pass


def main(io_manager: PatrimonyIOManager):
    """Patrimony administrator entry point"""

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
           show_all_itens(io_manager)

        elif option == "2":
            print("Triggering code to show balance sheet (to implement)")

        elif option == "3":
            print("Triggering code to show new flow and total value (to implement)")

        elif option == "4":
            print("Triggering code to add item (to implement)")

        elif option == "5":
            read_item(io_manager)

        elif option == "6":
            print("Triggering code to update item (to implement)")

        elif option == "7":
            print("Triggering code to subtract item (to implement)")

        elif option == "0":
            print("Exiting program ...")
            on = False

        else:
            print("Invalid option!")


if __name__ == "__main__":

    PATRIMONY_FILE = f"{os.path.dirname(__file__)}/patrimony.json"
    io_manager = PatrimonyIOManager(PATRIMONY_FILE)

    main(io_manager)

