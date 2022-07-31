#Updated to add a __str__ and change name to email in the __str__ and __repr__

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
            if item.name == item_name:

                return item


    def add_item(self, item):
        self.watchlist.append(item)

    def remove_item(self, item_name):

        for item in self.watchlist:
            if item.name == item_name:
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
