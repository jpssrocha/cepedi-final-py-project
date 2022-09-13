from .patrimony_io_manager import PatrimonyIOManager

class PatrimonyLogicManager:
    
    def __init__(self, io_manager: PatrimonyIOManager) -> None:
        self.io_manager = io_manager


    def calculate_net_cash_flow(self):
        """Go through patrimony items and calculated the net cash flow"""
        pass

    def calculate_net_value(self):
        """Go through patrimony items and calculated the net value"""
        pass
        

