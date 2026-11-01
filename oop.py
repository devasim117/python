from abc import ABC, abstractmethod

class Product(ABC):
    def __init__(self, name: str, base_price: float):
        self.name = name
        self.__base_price = base_price

    def get_base_price(self) -> float:
        return self.__base_price

    @abstractmethod
    def getPrice(self):
        pass


class PhysicalProduct(Product):
    def __init__(self, name: str, base_price: float, weight_kg: float):
        super().__init__(name, base_price)
        self.weight_kg = weight_kg

    def getPrice(self) -> float:
        return self.get_base_price()

    def __str__(self):
        return f"Hello "

pp1 = PhysicalProduct("Laptop", 13000.1, 1.4)
print(f"sdf {pp1.getPrice()}")
print(f"sdf {pp1}")

if 'Hello' == "Hello":
    print("equal")