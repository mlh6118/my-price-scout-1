
class User:
    def __init__(self, email, phone_number, cell_carrier, watchlist=[]):
        self.email = email
        self.phone_number = phone_number
        self.cell_carrier = cell_carrier
        self.watchlist = watchlist

    def __repr__(self):

        return f"email: {self.name}, phone number: {self.phone_number}, cell carrier: {self.cell_carrier}, items: {self.watchlist}"

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

                return f"{item} removed"

        return f"Item with name: {item_name} not found"

    def replace_item(self, old_item_name, item):
        old_item_idx = self.watchlist.index(old_item_name)
        self.watchlist[old_item_idx] = item

    def get_watchlist(self):

        return self.watchlist
