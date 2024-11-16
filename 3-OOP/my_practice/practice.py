class Microwave:
    def __init__(self, brand:str, power_rating:str)-> None:
        self.brand = brand
        self.power_rating = power_rating
        self.turned_on = False

    # Methods
    # Turn on Microwave
    def turn_on(self):
        if self.turned_on:
            print(f"Microwave ({self.brand}) is already turned on!")
        else:
            self.turned_on = True
            print(f"Microwave ({self.brand}) is now turned on!")
    
    # turn off microwave
    def turn_off(self):
        if self.turned_on:
            self.turned_on = False
            print(f"Microwave ({self.brand}) is now turned off!")
        else:
            print(f"Microwave ({self.brand}) is already turned off!")

    
    def run(self, seconds: int):
        if self.turned_on:
            print(f'Running ({self.brand}) for {seconds} seconds')
        else:
            print('Turn on the microwave first!!')



smeg = Microwave("Smeg", "B")
smeg.turn_on()
smeg.run(60)
smeg.turn_off()

bosch = Microwave('Bosch', "C")
