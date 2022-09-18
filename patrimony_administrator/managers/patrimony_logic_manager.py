from typing import Type

from patrimony_administrator.patrimony_items.patrimony_fabric import IMPLEMENTED_ASSETS, IMPLEMENTED_LIABILITIES, checkin_dict
from patrimony_administrator.patrimony_items.patrimony_item import PatrimonyItem
from patrimony_administrator.managers.patrimony_io_manager import PatrimonyIOManager

from datetime import datetime
from tabulate import tabulate


ITEMS = {**IMPLEMENTED_ASSETS, **IMPLEMENTED_LIABILITIES}

class PatrimonyLogicManager:
    
    def __init__(self, io_manager: PatrimonyIOManager) -> None:
        self.io_manager = io_manager
        
        loaded_items = []


        for item in io_manager.items.values():
            class_ = ITEMS[item["type"]]
            loaded_items.append(_instatiate_class_from_dict(item, class_))

        self.loaded_items: list[PatrimonyItem] = loaded_items


    def calculate_net_cash_flow(self):
        """Go through patrimony items and calculate the net cash flow"""
        total_cash_flow = sum([item.cash_flow for item in self.loaded_items])
        return total_cash_flow


    def calculate_net_value(self):
        """Go through patrimony items and calculate the net value"""
        total_value = sum([item.estimated_value for item in self.loaded_items])
        return total_value


    def print_balance_sheet(self):

        today = datetime.today().date()

        assets = list(filter(lambda item: item.type == "asset", self.loaded_items))
        liabilities = list(filter(lambda item: item.type == "liability", self.loaded_items))


        # Getting totals
        total_inflow = sum([item.cash_flow for item in assets])
        total_outflow = sum([item.cash_flow for item in liabilities])

        # Total value
        total_asset_value = sum([item.estimated_value for item in assets])
        total_liability_value = sum([item.estimated_value for item in liabilities])
        
        # Lines
        header = ["Description", "Estimated Value", "Cash Flow"]
        sep_line = ["-"*len(i) for i in header]

        asset_lines = [ [asset.description, asset.estimated_value, asset.cash_flow] for asset in assets]
        liability_lines = [ [liability.description, liability.estimated_value, liability.cash_flow] for liability in liabilities]

        asset_lines.append(sep_line)
        asset_lines.append(["Total", total_asset_value, total_inflow])



        liability_lines.append(sep_line)
        liability_lines.append(["Total", total_liability_value, total_outflow])



        body = f"""

Patrimonial Balance at {today.strftime("%d-%m-%Y")}
=================================

Assets
======

{tabulate(asset_lines, header)}
                

Liabilities
===========

{tabulate(liability_lines, header)}


Net Status
==========

Net value: {self.calculate_net_value()}
Net flow: {self.calculate_net_cash_flow()}
Status: {"Getting Rich" if self.calculate_net_cash_flow() > 0 else "Getting poorer"}
"""

        print(body)
        

def _instatiate_class_from_dict(dict_: dict, desired_class: Type[PatrimonyItem]) -> Type[PatrimonyItem] | None:
    """Given a dictionary instatiate a desired_class class from it"""

    # Check if all keys are present
    check = checkin_dict(desired_class.__slots__, dict_)

    if check:
        return desired_class(**{key: dict_[key] for key in desired_class.__slots__})

    print("Check failed. Some necessary keys aren't on the dictionary")


def tests():

    io_manager = PatrimonyIOManager(database_file_path="patrimony.json")

    logic_manager = PatrimonyLogicManager(io_manager)

    logic_manager.print_balance_sheet()



if __name__ == "__main__":
    tests()

