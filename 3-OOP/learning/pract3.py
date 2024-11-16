# CLASS ATTRIBUTES 
# its an attribute that belongs to the class (global attribute)
class Item:
    pay_rate = 0.8 #the pay rate after 20% discount

    # Class constructor Function
    def __init__(self, brand: str, price:float, qty: int) -> None:
        # run validation to the recieved arg
        assert price >= 0, f"Price ({self.price}) must be greater than 0 !!"
        assert qty >= 0, f"Quantity ({self.qty}) must be 1 or greater than 1 !!"
        
        # self allows us to attach parametors to the class
        # Assign to self object(attribute)
        self.brand = brand
        self.price = price 
        self.qty = qty 

    # Object Method(class attribute)
    def total_price(self):
        return self.price * self.qty

    def discount(self):
        self.price = self.price * self.pay_rate

# Object
item1 = Item("Iphone", 100, 5)
print(item1.total_price())

item2 = Item("Iphone", 500, 2)
item2.discount()
print(item2.price)

item3 = Item("Iphone", 500, 2)
item3.pay_rate = 0.7
item3.discount()
print(item3.price)

item4 = Item("Iphone", 500, 1)
item4.pay_rate = 0.7
item4.discount()
print(item4.price)