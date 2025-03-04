import os
import csv

from functions import c
from class_item import item


#Instantiate the items from CSV
item.instantiate_from_csv()


#Clear screen before program start
c()

#Printing the item list after instantiating them from CSV.
print("\nItem List :\n\t"+(str)(item.list_item))