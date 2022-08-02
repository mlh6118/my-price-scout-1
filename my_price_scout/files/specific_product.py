# Specific Product is the Object formerly known as Link

class Specific_Product():
    """This is the class that stores the url, website (amazon, target, OR walmart) and the price that is returned from the scraper. ONE WEBSITE LINK per specific product instance. Each product can have up to three specific product instances."""
    def __init__(self, website, url, price) -> None:
        self.website = website
        self.url = url
        self.price = price

    def __repr__(self):
        return f'Specific_Product(Website: {self.website}, URL: {self.url}, Price: {self.price})'

    def __str__(self):
        return f'(Website = {self.website}, url = {self.url},  current price = {self.price})'


    