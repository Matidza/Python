# CLASS ATTRIBUTES 
# its an attribute that belongs to the class (global attribute)

class Item:
    pay_rate = 0.8 #the pay rate after 20% discount

    # Class constructor Function
    def __init__(self,name:str,  price:float, qty=0):
        # run validation to the recieved arg
        assert price >= 0, f'Price {price} must be positive!!'
        assert qty >= 0 , f'Qty {qty} must be positive!!'
        
        # self allows us to attach parametors to the class
        # Assign to self object(attribute)
        self.price = price 
        self.qty = qty 
        self.name = name
      

    # Object Method(class attribute)
    def calculate_total_price(self):
        return  self.name , self.price * self.qty
    
    def apply_discount(self):
        self.price = self.price * self.pay_rate

# Object
item1 = Item("Iphone", 100, 5)
item1.apply_discount()
print(item1.price)


item2= Item("Iphone", 100, 5)
item2.pay_rate = 0.7 # applying a specific discount on a certain item and not all items
item2.apply_discount()
print(item2.price)