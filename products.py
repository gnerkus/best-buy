class Product:
    def __init__(self, name: str, price=0.0, quantity=1):
        if not isinstance(name, str):
            raise TypeError("Product name should be a string")
    
        if not name:
            raise ValueError("Product name is missing")
        
        self.name = name
        self.price = price
        self.quantity = quantity
        self.active = True

    def __str__(self) -> str:
        return f"{self.name}, Price: {self.price}, Quantity: {self.quantity}"
    
    def get_quantity(self) -> int:
        return self.quantity


    def set_quantity(self, quantity):
        if quantity < 0:
            raise ValueError("Quantity must be positive")
        
        if quantity == 0:
            self.active = False

        self.quantity = quantity


    def is_active(self) -> bool:
        return self.active
    
    def activate(self):
        self.active = True

    def deactivate(self):
        self.active = False

    def show(self) -> str:
        return self.__str__()
    
    def buy(self, quantity) -> float:
        new_quantity = max(self.quantity - quantity)
        self.set_quantity(new_quantity)
        return self.price * self.quantity

    
# test code
# =============================
# p = Product(2)
# print(p)
