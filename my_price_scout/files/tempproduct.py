#File Structure:
#   * add_specific_product: inputs - Specific Product Object, output - confirmation string  (may need to 
#     break this out to individual links)
#   * product_url_count: inputs - name, output - int
#   * remove_url: inputs - Link aka specific product, output - confirmation 
#   * add_name: inputs - name, output - confirmation string
#   * add_target_price: - inputs - int, output - confirmation string
#     string
#   * is_product_being_tracked: inputs - boolean, output - string about tracking, 
#     returns boolean (this should toggle tracking)
#   * get_summary: inputs - name, output - all data for the item (representation)
#   * change_url: inputs - website name, output - confirmation, calls 
#     remove_url followed by add_url



# Changes: in the init product name and target price are reversed
# Proposed changes- can remove_url handle in the logic of checking product_url_count?
# Can we use the str instead of get_summary?
# Can we add a str with ProductName, Target Price, Product List?



class Product:
    # Changed the order in the init file
    def __init__(self, product_name,target_price,
                 is_product_being_tracked=True,
                 specific_product_list=[]):
        self.product_name = product_name
        self.is_product_being_tracked = is_product_being_tracked
        self.specific_product_list = specific_product_list
        self.target_price = target_price

    def __repr__(self):
        return f"{self.specific_product_list}, Product Name:" \
               f" {self.product_name}, Target Price: {self.target_price}, Notifications: {self.is_product_being_tracked}"
        # Repr needs notifications

    def __str__(self):
        return f"Product Name: {self.product_name}, Target Price: {self.target_price}, {self.specific_product_list},"

    def add_specific_product(self, specific_product):
        """
        Arguments:
            self: specific instance of the Product class
            specific_product: object consisting of product_name, websites, urls,
            and actual_price.
        Return:
            confirmation_string: confirms the specific_product was added.
        """
        # Add instance specific_product that will live within the
        # product.links[].
        self.specific_product_list.append(specific_product)

    def product_url_count(self, product_name):
        """
        Arguments:
            product_name: product to get the url count for.
        Return:
            int: total number of urls between 1 and 3 for a given product.
        """
        count = 0
        for specific_product in self.specific_product_list:
            if specific_product.url:
                count += 1
            return count

    def remove_url(self, website):
        """
        Arguments:
             website: The website to remove the link for.  The values may be
             'amazon,' 'target,' or 'walmart'.
        Return:
            string: Confirmation that the method worked.
        """
        for specific_product in self.specific_product_list:
            if website == specific_product.website:
                self.specific_product_list.remove(specific_product)

                return f"{specific_product} removed."

        return f"Specific product on {website} not found."

    def get_summary(self):
        pass
