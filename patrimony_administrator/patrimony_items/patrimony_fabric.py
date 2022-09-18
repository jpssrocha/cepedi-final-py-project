from typing import Type

from patrimony_administrator.patrimony_items.patrimony_item import PatrimonyItem
from patrimony_administrator.patrimony_items.simple_patrimony_item import SimplePatrimonyItem

IMPLEMENTED_ASSETS = {"SimplePatrimonyItem" : SimplePatrimonyItem}
IMPLEMENTED_LIABILITIES = {"SimplePatrimonyItem" : SimplePatrimonyItem}


def checkin_dict(keys: list[str], dict_ : dict) ->  bool:
    """Check if all the strings in `keys` are in the `dict` keys"""
    return all([True if key in dict_.keys() else False for key in keys])


def checkin_dict_partial(keys: list[str], dict_ : dict) ->  bool:
    """Check if all the strings in `keys` are in the `dict` keys"""
    return any([True if key in dict_.keys() else False for key in keys])


def create_from_class_by_user_input(desired_class: Type[PatrimonyItem]) -> dict:
    """Create a dict for instantiating a given class by taking user input"""

    dict_template = {}
    for attribute, type_ in zip(desired_class.__slots__, desired_class.types):
        dict_template[attribute] = type_(input(f"Please input the attribute: `{attribute}` = ").strip())

    return dict_template


def instatiate_class_from_dict(dict_: dict, desired_class: Type[PatrimonyItem]) -> Type[PatrimonyItem] | None:
    """Given a dictionary instatiate a desired_class class from it"""

    # Check if all keys are present
    check = checkin_dict(desired_class.__slots__, dict_)

    if check:
        return desired_class(**{key: dict_[key] for key in desired_class.__slots__})

    print("Check failed. Some necessary keys aren't on the dictionary")


def tests():
    # create_from_class_by_user_input(SimplePatrimonyItem)
    # print(instatiate_class_from_dict({"bla": "bla"}, SimplePatrimonyItem))
    x = (instatiate_class_from_dict({"monthly_cash_flow": 1, "value": 1, "description": "bla"}, SimplePatrimonyItem))
    print(dir(x))
     

if __name__ == "__main__":
    tests()

        
