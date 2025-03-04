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
    #A list to track all items
    list_item = []
    
    #Creating a class attribute.
    discount = 0.1

    def __init__(self, name : str, price : float, quantity=0):
        #Append to the list.
        item.list_item.append(self)
        
        
        self.name = name
        self.price = price 
        self.quantity = quantity

        #Using assert to get the correct arguments.
        assert price>=0, "Price cannot be negative."
        assert quantity>=0, "Quantity cannot be negative,"

        print(f"-------------\nItem Declared\n-------------\n\tName : {self.name.capitalize()}\n\tPrice : {self.price}\n\tQuantity : {self.quantity}")
        

    
    #Using the __repr__ method to return a custom string for each item, That would be used in the list_item.
    def __repr__(self):
        return f"Class : {self.__class__.__name__} ->  {self.name.title()}"


    def method_total_price(self):
        return self.price*self.quantity

    def method_individual_discounted_price(self):
        return self.price*(1.0-self.discount)

    def method_apply_discount(self,discount_0_to_1):
        assert discount_0_to_1>=0 and discount_0_to_1<=1, "Discount can only be between 0 and 1 (Both Inclusive)"
        self.discount = discount_0_to_1

    #To display items of specific class only.
    @classmethod
    def items_by_class(cls, specific_class):
        return [a for a in cls.list_item if isinstance(a, specific_class)]  #List comprehension 

    



class laptop(item):
    def __init__(self, name, price, quantity=0, quantity_damaged=0):
        super().__init__(name, price, quantity)

class mobile(item):
    def __init__(self, name, price, quantity=0, quantity_damaged=0, is_5G=False):
        super().__init__(name, price, quantity)




"""
    Main Program
"""


#Clear screen before program start
c()

#Instantiasing.
laptop1 = laptop("lenovo", 32000, 6, 1)
laptop2 = laptop("apple", 52000, 2,0)
phone1 = mobile("one plus", 28000, 15, 4, True)
phone2 = mobile("samsung", 100000, 2,0, False)
print("\n")




print("Laptops :" , item.items_by_class(laptop))
print("Mobiles :", item.items_by_class(mobile))
