"""
Entry point for this patrimony administrator application
"""
import json
import os

from patrimony_administrator.managers.patrimony_io_manager import PatrimonyIOManager
from patrimony_administrator.managers.patrimony_logic_manager import PatrimonyLogicManager
from patrimony_administrator.patrimony_items.patrimony_fabric import IMPLEMENTED_ASSETS, IMPLEMENTED_LIABILITIES, create_from_class_by_user_input


def show_all_itens(io_manager: PatrimonyIOManager):
    """
    Show all patrimony items in a condensed view. Only the most relevant
    information.
    """
    print()
    print(io_manager)


def show_balance_sheet(io_manager: PatrimonyIOManager):
    """Show a balance sheet from the patrimony items"""

    logic_manager = PatrimonyLogicManager(io_manager)
    logic_manager.print_balance_sheet()



def show_net_and_value(io_manager: PatrimonyIOManager):
    """Show aggregated net flow and value of patrimony items"""
    logic_manager = PatrimonyLogicManager(io_manager)

    print(f"Net flow: {logic_manager.calculate_net_cash_flow()}")
    print(f"Net value: {logic_manager.calculate_net_value()}")


def _choose_item_menu(type_):
    """Menu to create a particular type of item"""

    options = {
            "asset": IMPLEMENTED_ASSETS,
            "liability": IMPLEMENTED_LIABILITIES
        }

    print(f"Here are the available kinds of {type_}: \n")
    
    for i, sub_type in enumerate(options[type_], start=1):
        print(f"{i}: {sub_type}")

    ordered = list(options[type_])

    question_index = int(input("\nWhich item number? (integer) "))

    while True:

        try: 
            item_class = ordered[question_index - 1]

            return options[type_][item_class], item_class

        except IndexError:
            print("IndexError: Please give a valid integer as option")


def _create(type_: str, io_manager: PatrimonyIOManager):

    item_class, item_class_name = _choose_item_menu(type_)

    basic_info = {"type" : item_class_name}
    print("\nObs: Use a minus sign to represent expenses or owed values\n")
    dict_representation = create_from_class_by_user_input(item_class)
    dict_representation.update(basic_info)
    io_manager.create_item(dict_representation)


def create_item(io_manager: PatrimonyIOManager):
    """Menu to create a new patrimony item from the user input"""

    negative_flow = input("Did this item make you pay cash directly? [y|n]: ")
    positive_flow = input("Did this item make you earn cash directly? [y|n]: ")

    match [negative_flow, positive_flow]:

        case ["y", "y"]:
            flow_direction = input("It makes more cash than expense? [y|n]: ")

            if flow_direction.lower() == "y":
                print("That's an asset")
                _create("asset", io_manager)
                
            else:
                print("That's a liability")
                _create("liability", io_manager)

        case ["n", "n"]:
            answer = input("Does it have monetary value? [y|n]")

            if answer.lower() == "y":
                print("That's an asset")
                _create("asset", io_manager)
            else:
                print("Not a patrimony item")
                
        case ["n", "y"]:
            print("That's an asset")
            _create("asset", io_manager)

        case ["y", "n"]:
            print("That's a liability")
            _create("liability", io_manager)

            

def read_item(io_manager: PatrimonyIOManager):
    """Read all info from patrimony item"""

    id_ = input("Which is the item id number? ")

    print(json.dumps(io_manager.read_item(id_), indent=4))


def update_item(io_manager: PatrimonyIOManager):
    """Update patrimony item properties"""
    id_ = input("Which is the item id number? ")

    item = io_manager.read_item(id_)

    if item:

        print("Patrimony item:")
        print(json.dumps(item, indent=4))

        
        try:

            update_dict = {}
            print("Press enter if do not want to update field")
            for attr in item:

                if attr not in ["id", "type"]:

                    answer = input(f"Update the `{attr}` field (current: {item[attr]}): ")

                    if answer:
                        answer = type(item[attr])(answer)
                        update_dict[attr] = answer

            io_manager.update_item(id_, update_dict)

        except Exception:
            print("Some problem ocurred")


def delete_item(patrimony_io_manager: PatrimonyIOManager):
    """Delete patrimony item menu"""

    id_ = input("Which is the item id number? ")

    print("Patrimony item:")
    item = patrimony_io_manager.read_item(id_)
    print(item)

    if item:

        answer = input(f"Are you sure that want to delete item: {id_}? [y|n]: ")

        if answer.lower() == "y":
            patrimony_io_manager.delete_item(id_)



def main(io_manager: PatrimonyIOManager):
    """Patrimony administrator entry point"""

    print(
        """
        Patrimony Administrator v0.1
        ----------------------------
        """
    )

    on = True

    while on:
        print(
        """
        Select option:

            0. Exit program
            1. Save changes
            2. See all items
            3. See balance sheet
            4. See net flow and patrimony value
            5. Create patrimony item
            6. Read patrimony item
            7. Update item
            8. Delete patrimony item
        """
        )

        option = input("Option: ")

        if option == "1":
            print(f"Saving changes to: {io_manager.database_file_path}")
            io_manager.commit_changes()
            
        elif option == "2":
           show_all_itens(io_manager)

        elif option == "3":
            show_balance_sheet(io_manager)
            
        elif option == "4":
            show_net_and_value(io_manager)

        elif option == "6":
            read_item(io_manager)

        elif option == "7":
            update_item(io_manager)

        elif option == "8":
            delete_item(io_manager)

        elif option == "5":
            create_item(io_manager)

        elif option == "0":
            answer = input("If not saved all progress will be lost. Confirm exiting? [y|n]: ")

            if answer.lower() == "y":
                print("Exiting program ...")
                on = False
            else:
                print("Returning ...")

        else:
            print("Invalid option!")


if __name__ == "__main__":

    PATRIMONY_FILE = f"{os.path.dirname(__file__)}/patrimony.json"
    io_manager = PatrimonyIOManager(PATRIMONY_FILE)

    main(io_manager)

