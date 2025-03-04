import csv

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
        
        #Custom attributes.
        # match name.lower() :
        #     case "laptop":
        #         NumPad_check = str(input("\tDoes Laptop has NumPad ? (True/false) : ")).capitalize()
        #         assert NumPad_check=="True" or NumPad_check=="False", "NumPad check accepts only true or false."
        #         self.has_numpad = bool (NumPad_check)
            
        #     case _ :
        #         pass

    
    #Using the __repr__ method to return a custom string for each item, That would be used in the list_item.
    def __repr__(self):
        return f"Item : {self.name.capitalize()}"


    # def method_total_price(self):
    #     return self.price*self.quantity

    # def method_individual_discounted_price(self):
    #     return self.price*(1.0-self.discount)

    # def method_apply_discount(self,discount_0_to_1):
    #     assert discount_0_to_1>=0 and discount_0_to_1<=1, "Discount can only be between 0 and 1 (Both Inclusive)"
    #     self.discount = discount_0_to_1



    """
        Trying to get objects from CSV. But this doesn't work as we alwaus have to pass self.
            def instantiate_from_csv(self):
        
        Hence making it a class method.
    """
    
    @classmethod
    def instantiate_from_csv(cls):
        with open ('items.csv', 'r') as f:
            items_from_csv = list(csv.DictReader(f))
        
        for a in items_from_csv :
            item(
                name=str(a.get("name")),
                price=float(a.get("price")),
                quantity=int(a.get("quantity"))
            )