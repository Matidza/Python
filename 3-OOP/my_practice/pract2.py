class Item:
    pay_rate = 0.8
    all = []

    def __init__(self, name: str, price: float, qty: int):
        # Validate the recieved arguments
        assert price >= 0, f"Price ({self.price}) must be greater than zero or equal to zero!"
        assert qty >= 0, f"Quantity ({self.qty}) must be greater than zero or equal to zero!"

        # Asign to self object
        self.name = name 
        self.price = price 
        self.qty = qty 

        Item.all.append(self)

    # Methods
    def total_price(self):
        return self.price * self.qty 
    
    def discount(self):
        self.price = self.price * self.pay_rate

    def __repr__(self) -> str:
        return f"Item('{self.name}', '{self.price}', '{self.qty}')"
        

# Object
item1 = Item("Phone", 100, 1)
item2 = Item("Laptop", 1000, 3)
item3 = Item("Cable", 10, 5)
item4 = Item("Mouse", 50, 5)
item5 = Item("Keyboard", 75, 5)

print(Item.all)