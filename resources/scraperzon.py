import requests
from bs4 import BeautifulSoup
import pandas as pd
from time import sleep

# Likely not quite working yet - not tested and needs to be linked/have functions exported for linking to main functions.

search_query = "winter jacket".replace('','+')

base_url = 'https://www.amazon.com/s?k={0}'.format(search_query)

URL = 'https://www.amazon.com/gp/product/B07NBQX8HS/ref=ox_sc_saved_title_2?smid=ATVPDKIKX0DER&psc=1'

def amazon_get_price():
    page = requests.get(URL)

    #print(page.content)

    soup = BeautifulSoup(page.content, "html.parser")

    response = requests.get(base_url + '&page={0'.format(i))
    soup = BeautifulSoup(response.content, 'html.parser')

    title = soup.find('id="productTitle').get_text()
    
    try:
        price = soup.find(id="priceblock_ourprice").get_text()
    except:
        # for pages with deal prices
        price = soup.find(id="priceblock_dealprice").get_text()

    converted_price = float(price[:-3])
    # This removes the change and the price currency character

    print(title.strip())

def price_compare():
    # This will need to take in the user input and should probably live on some central page for all scraper functions
    strike_price = 0
    converted_price = 0 
    # Converted price should be the return from the scraper
    if (converted_price<strike_price):
        pass
        #notification_function_call()
        # root.after(int(600000), check_price)
        # Checks the price every 10 minutes. Not sure this root function will work as it is written. 

