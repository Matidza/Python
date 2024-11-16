class Item:
    # Class constructor Function
    def __init__(self,name:str,  price:float, qty=0):
        # run validation to the recieved arg
        assert price >= 0, f'Price {price} must be positive!!'
        assert qty >= 0 , f'Qty {qty} must be positive!!'
        
        # self allows us to attach parametors to the class
        # Assign to self object
        self.price = price 
        self.qty = qty 
        self.name = name
      

    # Object Method
    def calculate_total_price(self):
        return  self.name , self.price*self.qty

# Object
item1 = Item("Iphone", 100, 5)
print(item1.calculate_total_price())