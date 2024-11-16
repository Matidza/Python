# CLASS ATTRIBUTES
# its an attribute that belongs to the class (global attribute)

class Item:
    pay_rate = 0.8  # the pay rate after 20% discount
    all = []

    # Class constructor Function
    def __init__(self, name: str,  price: float, qty=0):
        # run validation to the recieved arg
        assert price >= 0, f'Price {price} must be positive!!'
        assert qty >= 0, f'Qty {qty} must be positive!!'

        # self allows us to attach parametors to the class
        # Assign to self object(attribute)
        self.price = price
        self.qty = qty
        self.name = name

        # Actions to execute
        Item.all.append(self)

    # Object Method(class attribute)

    def calculate_total_price(self):
        return self.name, self.price * self.qty

    def apply_discount(self):
        self.price = self.price * self.pay_rate

    def __repr__(self):
        return f"Item('{self.name}', '{self.price}', '{self.qty}')"

    """"
    def __str__(self):
        return self.name
    """ 
    


# Object
item1 = Item("Phone", 100, 1)
item2 = Item("Laptop", 1000, 3)
item3 = Item("Cable", 10, 5)
item4 = Item("Mouse", 50, 5)
item5 = Item("Keyboard", 75, 5)


print(Item.all) # printing all items in the list

#for instance in Item.all:
#   print(f"{instance.name}: R{instance.price}")


