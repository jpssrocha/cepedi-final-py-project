from .patrimony_item import PatrimonyItem

class SimplePatrimonyItem(PatrimonyItem):

    __slots__ = ["monthly_cash_flow", "value", "description"]
    types     = [float, float, str]

    def __init__(self, monthly_cash_flow: float, value: float, description: str) -> None:

        self.monthly_cash_flow = monthly_cash_flow
        self.value = value
        self.description = description


    @property
    def cash_flow(self) -> float:
        return self.monthly_cash_flow


    @property
    def estimated_value(self) -> float:
        return self.value 


def tests():
    dict_ = {
        "monthly_cash_flow": 1,
        "value": 1,
        "description": "bla"
    }

    print(SimplePatrimonyItem(**dict_).to_dict())
    print(SimplePatrimonyItem.__slots__)

if __name__ == "__main__":
    tests()

