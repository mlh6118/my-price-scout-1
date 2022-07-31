import link
# import DBUtils


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

# specific_product is the product_name, website, url, and actual_price.  This is
# passed in by App.

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


class SpecificProduct:
    def __init__(self, website, url):
        self.website = website
        self.url = url

    def __repr__(self):
        return f"{self.website}: {self.url}"


if __name__ == '__main__':
    specific_product = SpecificProduct("target", "abcd")
    specific_product2 = SpecificProduct("walmart", "xyz")
    print(specific_product)
    new_product = Product(150, "TV")
    # print(new_product)
    new_product.add_specific_product(specific_product)
    new_product.add_specific_product(specific_product2)
    # print(new_product.specific_product_list[0])
    print(new_product)
    new_product.remove_url('target')
    print(new_product)
