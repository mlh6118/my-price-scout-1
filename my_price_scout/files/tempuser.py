#Updated to add a __str__ and change name to email in the __str__ 
# Updated the repr to have just the user information
# Line 32 needs to be changed since it is called product_name in the products file. Function is still coming back as not defined.

from tempproduct import Product

class User:
    def __init__(self, email, phone_number, cell_carrier, watchlist=None):
        self.email = email
        self.phone_number = phone_number
        self.cell_carrier = cell_carrier
        self.watchlist = watchlist if watchlist else []


    def __repr__(self):

        return f"email: {self.email}, phone number: {self.phone_number}, cell carrier: {self.cell_carrier}, items: {self.watchlist}"

    def __str__(self):

        return f"email: {self.email}, phone number: {self.phone_number}, cell carrier: {self.cell_carrier}, items: {self.watchlist}"

    def get_item(self, item_name):
        for item in self.watchlist:
            if item.product_name == item_name:
                return item


    def add_item(self, item):
        self.watchlist.append(item)

    def remove_item(self, item_name):

        for item in self.watchlist:
            #!!!!!!!!!!!!!!!!!!!!CHANGE!!!!!!!!!! item.name needs to be item.product_name
            if item.product_name == item_name:
                self.watchlist.remove(item)


    def replace_item(self, old_item_name, item):
        new_watchlist = []
        
        for old_item in self.watchlist:
          if old_item.name == old_item_name:
            new_watchlist.append(item)
          else:
            new_watchlist.append(old_item)
        
        self.watchlist = new_watchlist

    def get_watchlist(self):

        return self.watchlist
