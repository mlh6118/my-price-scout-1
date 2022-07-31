# Project Framework
#   * get_or_create_user: inputs - email, phone, carrier, outputs - User instance
#     * helper methods: get_user, create_user, save_user
#     * save_user will parse the User instance into key values and save to Db 
#       using Database Utils
#   * start: inputs - none, outputs - screen prompts or return information
#     * helpers: IO Utils, User, and Item
#   * menu: Routing the user through the options they have available. inputs - None outputs - function calls based on the users selections.(Different options for where they would like to go and some sort of back function)
# 
# * remove_url: calls the remove_url method in Item
#     * inputs - website name (i.e., Amazon), outputs - confirmation 
#       string
#     * if removing the only link, then prompt user for new link or to 
#       remove item
#   * manage_user_items: logic for when a user has items to add, remove, or 
#     edit items

# To Do :
# create a menu for the user with the options for the things they can change. Create methods that call the other class' functions that hold those methods 
# Create the board that gives the other classes the info they need/build out the user with the products and build out the products with the specific products

import sys
from ioutils import IOUtils
from tempDBUtils import DBUtils
from user import User
from tempproduct import Product
from specific_product import Specific_Product
from tempscraper import Scraper
from temptracker import Tracker


class App_Logic:
    def __init__(self) -> None:
        self.user_inputs = IOUtils()
        self.database = DBUtils()
        self.scraper = Scraper()
        self.tracker = Tracker()
        self.user = None
        self.user_data = {}
        self.product = None
        self.specific_product = None


    def start(self):
        """This method displays the original user welcome and introduces them to how to quit. THis is where the user interface lives and calls functions to handle the inputs and route the user."""
        
        print("Welcome to My Price Scout where you can track product pricing from Amazon, Walmart, and Target!\nPress q to quit at any time")

        self.get_or_create_new_user()
        
        self.manage_user_items_menu()


    def get_or_create_new_user(self):
        """Takes in the users email as an input and checks the database for the user. Routes to create a new user or return user information based on Database returned info."""

        email = self.user_inputs.capture_email()
        print(email)

        if self.database.get_data(email) == None:
            self.create_user(email)
        else:
            self.get_user(email)


    def create_user(self, email):
        print("Welcome new user! Let's get you set up with an account!")
        
        number = self.user_inputs.capture_number()
        carrier = self.user_inputs.capture_carrier()

        self.user = User(email, number, carrier)

        print (self.user)

        self.save_user()
        

    def save_user(self):
        """Parse the data from the users input and send it to the DBUtils as an object"""
        self.user_data = {self.user.email: {
            "email": self.user.email,
            "phone_number": self.user.phone_number,
            "cell_carrier": self.user.cell_carrier,
            "watchlist": self.user.watchlist
            }
        }
        self.database.set_data(self.user_data)


    def get_user(self, email):
        """Parse the data from the database and make a new user object"""
        #This is where we need to set up the retrieval for the user object - depends on how we input the user information
        
        if self.database.get_data(email) is None:
            return None
        
        else:
            print("Welcome back!")

            self.user_data = self.database.get_data(email)

            number = self.user_data[email]["phone_number"]
            carrier = self.user_data[email]["cell_carrier"]
            watchlist = self.user_data[email]["watchlist"]

            self.user = User(email, number, carrier, watchlist)
        
    

    def manage_user_items_menu(self):
        # See the example Sergii sent
        print("Main Menu")
        pass

# import keyboard
#     keyboard.add_hotkey('q', lambda: quit())
#     exitProgram=False

#     def quit():
#         global exitProgram
#         exitProgram=True

    def keyboard_quit(self, message):
        sys.exit(message)


if __name__ == "__main__":
    try:
        new_app = App_Logic()
        new_app.start()
    except KeyboardInterrupt:
        new_app.keyboard_quit('You have pressed CTRL-C so Goodbye!')
