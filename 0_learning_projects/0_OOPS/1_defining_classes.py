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
    #To recieve only a certain class as argument ->  argument : required_class
    def __init__(self, name : str, price : float , quantity=0):
        self.name = name
        self.price = price 
        self.quantity = quantity

        print(f"-------------\nItem Declared\n-------------\n\tName : {self.name.capitalize()}\n\tPrice : {self.price}\n\tQuantity : {self.quantity}\n")


"""
    Main Program
"""


#Clear screen before program start
c()


item1 = item("mouse", 200, 4)
item2 = item("keyboard", 400, 2)


"""
        Output 

        -------------
        Item Declared
        -------------
                Name : Mouse
                Price : 200
                Quantity : 4

        -------------
        Item Declared
        -------------
                Name : Keyboard
                Price : 400
                Quantity : 2

"""