# IO Utils Class Project Framework

#   * Capture email: inputs - email, outputs - validated email 
#   * Capture phone: inputs - phone, outputs - validated phone
#   * Capture carrier: inputs - carrier, validated carrier
#   * Capture url: inputs - url, validated url --> Also pass to the correct scraper function
#   * Capture the 

import sys
import re

class IOUtils:
    """This is the class that validates all of the user inputs"""
    def __init__(self) -> None:
        pass

    def quit_app(self):
        print(f"Thanks checking in, see you next time!")
        sys.exit(1)

    def check(self, value):
        print(f"Is {value} right? Type y or n")
        verify = input("> ").lower()
        if verify == "q":
            self.quit_app()
        if verify =="y":
            return value
        if verify == "n":
            print("Please enter again")
            return None


    def capture_email(self):
        """Capture email: inputs - email, outputs - validated email """

        email = input("> ").lower()
        
        if email == "q":
            self.quit_app()

        regex_email = r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+'
        
        if (re.fullmatch(regex_email, email)):
            email = self.check(email)
            if email is None:
                self.capture_email()
            else:
                # print(email)
                return email
            
        else:
            print("Invalid Email\nPlease try to input your email again")
            email=None
            self.capture_email()


    def capture_number(self):
        """Capture number: inputs - 10 digit phone number, outputs - validated number """

        number = input("> ").lower()

        if number == "q":
            self.quit_app()

        regex_number = r'(\d{3})[-. ]*(\d{3})[-. ]*(\d{4})\S+'

        if (re.fullmatch(regex_number, number)):
            number = self.check(number)
            if number is None:
                self.capture_number()
            else:
                # print(number)
                return number
            
        else:
            print("Invalid number\nPlease try to input your number again")
            number=None
            self.capture_number()


    def capture_carrier(self):
        """Capture cell phone carrier: inputs - carrier, outputs - String"""

        phone_plan = input("> ").lower()
        
        if phone_plan == "q":
            self.quit_app()

        list_of_carriers = ["ATT", "BOOST", "CRICKET", "GOOGLEFI", "METROPCS", "MINT", "SIMPLEMOBILE", "SPRINT", "TMOBILE", "VERIZON", "VIRGIN", "XFINITY"]
        
        if phone_plan in list_of_carriers:
            phone_plan = self.check(phone_plan)
            if phone_plan is None:
                self.capture_carrier()
            else:
                # print(phone_plan)
                return phone_plan

    def capture_carrier(self):
        """Capture up to 3 URLs for product"""

        print("Please choose from the following phone plan.\nATT, BOOST, CRICKET, GOOGLEFI, METROPCS, MINT, SIMPLEMOBILE, SPRINT, TMOBILE, VERIZON, VIRGIN, XFINITY\nIf your provider is not listed, we do not support your carrier at this time. Please press q to exit")

        phone_plan = input("> ").lower()
        
        if phone_plan == "q":
            self.quit_app()

        list_of_carriers = ["ATT", "BOOST", "CRICKET", "GOOGLEFI", "METROPCS", "MINT", "SIMPLEMOBILE", "SPRINT", "TMOBILE", "VERIZON", "VIRGIN", "XFINITY"]
        
        if phone_plan in list_of_carriers:
            phone_plan = self.check(phone_plan)
            if phone_plan is None:
                self.capture_carrier()
            else:
                # print(phone_plan)
                return phone_plan
            
        else:
            print("Invalid phone_plan\nPlease try to input your phone_plan again")
            phone_plan=None
            self.capture_phone_plan()


    def capture_url(self):
        """Capture up to 3 URLs for product and address which scrape function needs to be called and call it"""

        print("Now we are going to have you input ")

        phone_plan = input("> ").lower()
        
        if phone_plan == "q":
            self.quit_app()

        list_of_carriers = ["ATT", "BOOST", "CRICKET", "GOOGLEFI", "METROPCS", "MINT", "SIMPLEMOBILE", "SPRINT", "TMOBILE", "VERIZON", "VIRGIN", "XFINITY"]
        
        if phone_plan in list_of_carriers:
            phone_plan = self.check(phone_plan)
            if phone_plan is None:
                self.capture_carrier()
            else:
                # print(phone_plan)
                return phone_plan
            
        else:
            print("Invalid phone_plan\nPlease try to input your phone_plan again")
            phone_plan=None
            self.capture_phone_plan()
        
