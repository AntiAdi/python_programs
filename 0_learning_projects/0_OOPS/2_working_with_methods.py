import os


"""
    Functions
"""

#Function to clear the screen.
def c():
    os.system("cls" if os.name=="nt" else "clear")


"""
    Classes
"""

class item():
    #The object itself is passed as the first parameter self.
    def __init__(self, name : str, price : float, quantity=0):
        self.name = name
        self.price = price 
        self.quantity = quantity
        print(f"-------------\nItem Declared\n-------------\n\tName : {self.name.capitalize()}\n\tPrice : {self.price}\n\tQuantity : {self.quantity}\n")

    def method_total_price(self):
        return self.price*self.quantity


"""
    Main Program
"""


#Clear screen before program start
c()


#Initialising Instances of Class item.
item1 = item("mouse", 200, 4)
item2 = item("keyboard", 400, 2)


print(f"Total Price of {item1.name.capitalize()} = {item1.method_total_price()}")
print(f"Total Price of {item2.name.capitalize()} = {item2.method_total_price()}")