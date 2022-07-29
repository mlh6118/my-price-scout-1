# My Price Scout

This app allows you to add desired items from different online retailers to a watchlist and set your desired price. The app will notify you when the item price drops to the desired level via text notification.

## Authors
Marni Hager, Jae Loney, Pedro Perez, Sergii Ottryshko

## User Stories
https://python401.atlassian.net/wiki/spaces/US/pages/590051/User+Stories+-+My+Price+Scout

## Database Schema

[“User”: {
“Email”:”” : String
 “PhoneNumber”: “” : Integers
“PhoneCarrier” : “” : String
“ProductsList”: [] : List[object]
}]
The products class gives each item the attributes below:
Product - Will have name/nickname(string), links to products(strings), current prices(integers), whether they are being tracked(Boolean), strike prices (integers).

## UML

See the UML drawing by clicking [here](images/my-price-scout-uml.png)

## Wireframe

See the wireframe [here](images/Wireframe-MyPriceScout.png)


## Resources
Email Validation: https://www.geeksforgeeks.org/check-if-email-address-valid-or-not-in-python/
Amazon Scraping: https://www.youtube.com/watch?v=DHqAQxgleoc&ab_channel=JieJenn
Amazon Scraping: https://www.youtube.com/watch?v=Bg9r_yLk7VY&ab_channel=DevEd
Amazon Scraping: https://github.com/ArkadiyReydman/Amazon-Walmart-Etsy-Price-Tracker/blob/master/price_tracker.py
