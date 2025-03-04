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
    def __init__(self, name : str, price : float, quantity=0):
        self.name = name
        self.price = price 
        self.quantity = quantity
        print(f"-------------\nItem Declared\n-------------\n\tName : {self.name.capitalize()}\n\tPrice : {self.price}\n\tQuantity : {self.quantity}")
        
        #Custom attributes.
        match name.lower() :
            case "laptop":
                NumPad_check = str(input("\tDoes Laptop has NumPad ? (True/false) : ")).capitalize()
                assert NumPad_check=="True" or NumPad_check=="False", "NumPad check accepts only true or false."
                self.has_numpad = bool (NumPad_check)
            
            case _ :
                pass





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
item3 = item("laptop", 25000, 1)
