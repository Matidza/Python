class Item:
    # Class constructor Function
    def __init__(self,name,  price, qty):
        # self allows us to attach parametors to the class
        self.price = price 
        self.qty = qty 
        self.name = name

    # Object Method
    def calculate_total_price(self):
        return  self.name , self.price*self.qty

# Object
item1 = Item("Iphone", 100, 5)
print(item1.calculate_total_price())