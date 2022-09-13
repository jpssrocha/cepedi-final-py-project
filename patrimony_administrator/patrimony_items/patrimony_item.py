from abc import ABC, abstractmethod

class PatrimonyItem(ABC):
    type_: str

    @property
    @abstractmethod
    def cash_flow(self):
        """Calculates the cash_flow generated by an item"""
        pass


    @property
    @abstractmethod
    def estimated_value(self):
        """Estimates the value of an item"""
        pass


    @abstractmethod
    def to_dict(self):
        """Return dictionary representation of the instance"""
        pass
