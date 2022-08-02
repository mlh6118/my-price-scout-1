import requests
from bs4 import BeautifulSoup
import re


class Scraper:

    def __init__(self, url=None):
        self.url = url

    def scrape_amazon(url):

        URL = url

        headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36", "Accept-Encoding": "gzip, deflate",
                   "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", "DNT": "1", "Connection": "close", "Upgrade-Insecure-Requests": "1"}

        page = requests.get(URL, headers=headers)

        soup1 = BeautifulSoup(page.content, "html.parser")

        soup2 = soup1.find_all(class_="a-offscreen")

        finds = re.findall(
            r'\$\d{1,3}(?:[,]\d{3})*(?:[.]\d{0,2})?|\d{1,3}(?:[ ]\d{3})*(?:[,]\d{0,2})?', str(soup2[0]))

        print(finds[0])

        return(finds[0])

    def scrape_target(url):

        URL = url

        page = requests.get(URL)

        soup1 = BeautifulSoup(page.content, "html.parser")

        soup2 = soup1.prettify()

        finds = re.findall(r'current_retail\\\"\:\d+(?:\.\d+)?', soup2)

        item_found = []

        for find in finds:
            item_found.append(find)

        if item_found is None:
            actual_price = "Price not available"
            return actual_price
        else:
            actual_price = re.findall(r'\d+(?:\.\d+)?', item_found[0])
            print(str("$"+actual_price[0]))
            return str("$"+actual_price[0])

    def scrape_walmart(url):

        URL = url

        headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36", "Accept-Encoding": "gzip, deflate",
                   "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", "DNT": "1", "Connection": "close", "Upgrade-Insecure-Requests": "1"}

        # page = requests.get(URL, headers=headers)

        # soup = BeautifulSoup(page.content, "html.parser")

        # print(soup.find_all(class_="b lh-copy dark-gray mr2 f1"))

        # soup2 = BeautifulSoup(soup1.prettify(), "html.parser")

        # finds = re.findall(r'current_retail\\\"\:\d+(?:\.\d+)?', soup2)

        # soup2 = soup1.find_all()

        # print(soup1.find_all())

        # item_found = []

        # for find in finds:
        #     item_found.append(find)

        # if item_found is None:
        #     actual_price = "Price not available"
        #     return actual_price
        # else:
        #     actual_price = re.findall(r'\d+(?:\.\d+)?', item_found[0])
        #     print(str("$"+actual_price[0]))
        #     return str("$"+actual_price[0])

        return 100


if __name__ == "__main__":

    Scraper.scrape_amazon(
        'https://www.amazon.com/APC-Battery-Protector-BackUPS-BX1500M/dp/B06VY6FXMM?ref_=Oct_DLandingS_D_d1d1e0d6_60&smid=ATVPDKIKX0DER&th=1')
    # Scraper.scrape_amazon(
    #     'https://www.amazon.com/dp/B07VHZ41L8?ref_=nav_em__k_ods_ha_ta_0_2_4_6')
    # Scraper.scrape_amazon(
    #     'https://www.amazon.com/dp/B08F6FYN6B?ref_=nav_em__k_ods_tab_ta_pls_0_2_5_6')
    # Scraper.scrape_amazon(
    #     'https://www.amazon.com/gp/product/B0B1352TDK?ie=UTF8&keywords=jewelry&sprefix=je%2Cluxury%2C151&sr=1-1&crid=2KWVNYXW3SHUW&qid=1659393999&ref_=sr_1_1_lx_bd')
    # Scraper.scrape_amazon(
    #     'https://www.amazon.com/Natural-Current-NC13KWDYIKIT-Floating-Installation/dp/B00R34C7GG/ref=sr_1_1?crid=2WCGEAFZOK0Z6&keywords=solar+panels&qid=1659395715&sprefix=solar+pa%2Caps%2C148&sr=8-1')
    # Scraper.scrape_amazon(
    #     'https://www.amazon.com/Napkins-Lucheon-Beverage-Guest-BIrthday/dp/B00JBG31KK/ref=sr_1_2?crid=258BO8L7ZNNWE&keywords=napkins&qid=1659396596&sprefix=napkins%2Caps%2C186&sr=8-2')

    # Scraper.scrape_target(
    #     'https://www.target.com/p/hisense-55-34-class-a6g-series-4k-uhd-android-smart-tv-55a6g/-/A-82802681#lnk=sametab')
    # Scraper.scrape_target(
    #     'https://www.target.com/p/sylvania-portable-cd-radio-boom-box/-/A-86782044#lnk=sametab')
    # Scraper.scrape_target(
    #     'https://www.target.com/p/goumikids-thermal-organic-cotton-pants/-/A-85165008?preselect=85165038#lnk=sametab')
    # Scraper.scrape_target(
    #     'https://www.target.com/p/pompeii3-2ct-huge-diamond-heart-pendant-14k-white-gold/-/A-87091390#lnk=sametab')
    # Scraper.scrape_target(
    #     'https://www.target.com/p/newair-27-built-in-160-bottle-dual-zone-compressor-wine-fridge-in-stainless-steel-quiet-operation-with-smooth-rolling-shelves/-/A-86737742#lnk=sametab')
    # Scraper.scrape_target(
    #     'https://www.target.com/p/disposable-paper-napkins-230ct-smartly-8482/-/A-75557241#lnk=sametab')

    # Scraper.scrape_walmart(
    #     'https://www.walmart.com/ip/Rayovac-High-Energy-AAA-Batteries-60-Pack-Triple-A-Batteries/45598335')
