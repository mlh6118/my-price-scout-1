import sys
from ioutils import IOUtils
from tempDBUtils import DBUtils

# Project Framework
#   * get_or_create_user: inputs - email, phone, carrier, outputs - User instance
#     * helper methods: get_user, create_user, save_user
#     * save_user will parse the User instance into key values and save to Db 
#       using Database Utils
#   * start: inputs - none, outputs - screen prompts or return information
#     * helpers: IO Utils, User, and Item
# 
# * remove_url: calls the remove_url method in Item
#     * inputs - website name (i.e., Amazon), outputs - confirmation 
#       string
#     * if removing the only link, then prompt user for new link or to 
#       remove item
#   * manage_user_items: logic for when a user has items to add, remove, or 
#     edit items



class App_Logic:
    def __init__(self) -> None:
        pass

    def start(self):
        """This method displays the original user welcome and introduces them to how to quit"""
        print("Welcome to My Price Scout where you can track product pricing from Amazon, Walmart, and Target!\nEnter your email to get started\Or press q to quit at any time")

        navigation = IOUtils()

        email = navigation.capture_email()

        if DBUtils.get_email(email) == None:
            self.create_user(email)
        else:
            self.get_user(email)

    def create_user(self, email):
        pass

        # See if the email is a user in the database
        # else:
            # print("Welcome New User!\nPlease enter your 10 digit phone number")
            # number = input("> ")
            # while not (re.fullmatch(regex_number, number)):
            #     print("Invalid Email\nPlease try to input your 10 digit number again")
            # print("Welcome New User!\nPlease enter your phone carrier")
            # carrier = input("> ")
            ## We will need to pass these items into the user class


    def get_user(email):
        print("Welcome back!")
        # self.return_user_object # This would not be self but would need to come back from the db utils



    # def return_user_object():
        #This is where we need to set up the retrieval for the user object - depends on how we input the user information
    




    def keyboard_quit(self, message):
        sys.exit(message)


if __name__ == "__main__":
    try:
        new_app = App_Logic()
        new_app.start()
    except KeyboardInterrupt:
        new_app.keyboard_quit('You have pressed CTRL-C so Goodbye!')
