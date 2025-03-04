"""
    Static methods can be used as regular isolated functions as well.
    But someone somehow had this this idea that they should have ability to
    be put with classes as well. 
    Nothing too fancy. Not rocket science.
"""



"""
    Classes
"""

class item():
    def __init__(self):
        pass
    
    #Static Method here.
    @staticmethod
    def is_integer(num):
        if isinstance(num, int):
            return True
        else:
            return False
    



"""
    Main Program
"""

#Static and Class methods both can be called from either instances or class. (absurd)
print(item.is_integer(3))
print(item.is_integer(5.5))



