# Class HW Assignment
# MIS 4322 - MW 1:00 - 2:15
# Noah Miller


#Create the class
class RetailItem:
    def __init__(self,desc,quantity,price):
        self.__Description        = desc
        self.__Inventory_Quantity = quantity
        self.__Price              = price

    def set_description(self, desc):
        self.__Description        = desc

    def set_inven_quantity(self, quantity):
        self.__Inventory_Quantity = quantity

    def set_price(self, price):
        self.__Price              = price

    #def return_item(self):
    #    return self.__Description, self.__Inventory_Quantity, self.__Price

    def __str__(self):
       return (
           "Item Description: " +
           str(self.__Description) + "\n" +
           "Inventory Quantity: " +
           str(self.__Inventory_Quantity) + "\n" +
           "Price: $" +
           str(self.__Price) + "\n"
       )

############################################################################
#Use the class

import RetailItemClass as ri 

def main():
    items = Item_ID()

    display_items(items)

    print("A list of the given items has been created for you.")
    print("Please check the folder where you saved this .py file.")
    print("The document is called: Items_List.txt")

    #desc, quantity, price = Item_ID()
    #Item1 = ri.RetailItem(desc,quantity,price)
    #print(Item1.return_item())
    
    #desc, quantity, price = Item_ID()
    #Item2 = ri.RetailItem(desc,quantity,price)
    #print(Item2.return_item())
    
    #desc, quantity, price = Item_ID()
    #Item3 = ri.RetailItem(desc,quantity,price)
    #print(Item3.return_item())

def Item_ID():
    item_list = []
    creation = int(input("How many items will you be creating today? "))
    for count in range(creation):
        desc        = input("Please enter the item's description: ")
        quantity    = int(input("Please enter the item's current invetory quantity: "))
        price       = float(input("Please enter the item's current price: "))
        print()
        item = ri.RetailItem(desc,quantity,price)
        item_list.append(item)
    return item_list

def display_items(items_list):
    for item in items_list:
        print(item.__str__())
        write_items(items_list)

def write_items(items_list):
    outfile = open("Items_List.txt","w")
    for item in items_list:
        outfile.write(item.__str__()+ "\n")
    outfile.close()
    

#def new_item_creation(desc,quantity,price):
#    desc        = input("Please enter the item's description: ")
#    quantity    = int(input("Please enter the item's current invetory quantity: "))
#    price       = float(input("Please enter the item's current price: "))
#    return(desc,quantity,price)
main()
