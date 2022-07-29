import sys
import re


class Menu:
    def __init__(self) -> None:
        pass

    def start():
        """This method displays the original user welcome and introduces them to how to quit"""
        print("Welcome to My Price Scout where you can track product pricing from Amazon, Walmart, and Target!\nEnter your email to get started")

        email = input("> ").lower()

        regex_email = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        regex_number = r'(\d{3})[-. ]*(\d{3})[-. ]*(\d{4})\S+'

        while not (re.fullmatch(regex_email, email)):
            print("Invalid Email\nPlease try to input your email again")

        # See if the email is a user in the database
        # if email in *database*
            # print("Welcome back!")
            # self.return_user_object
        # else:
            # print("Welcome New User!\nPlease enter your 10 digit phone number")
            # number = input("> ")
            # while not (re.fullmatch(regex_number, number)):
            #     print("Invalid Email\nPlease try to input your 10 digit number again")
            # print("Welcome New User!\nPlease enter your phone carrier")
            # carrier = input("> ")
            ## We will need to pass these items into the user class



    # def return_user_object():
        #This is where we need to set up the retrieval for the user object - depends on how we input the user information
    

    # q to quit should be in the main menu


    def keyboard_quit(self, message):
        sys.exit(message)


if __name__ == "__main__":
    try:
        new_menu = Menu()
        new_menu.start()
    except KeyboardInterrupt:
        new_menu.keyboard_quit('You have pressed CTRL-C so Goodbye!')


