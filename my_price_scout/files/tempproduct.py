
class Product:
    def __init__(self, target_price, product_name,
                 is_product_being_tracked=True,
                 specific_product_list=[]):
        self.product_name = product_name
        self.is_product_being_tracked = is_product_being_tracked
        self.specific_product_list = specific_product_list
        self.target_price = target_price

    def __repr__(self):
        return f"{self.specific_product_list}, Product Name:" \
               f" {self.product_name}, Target Price: {self.target_price}"

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
