# My Price Scout

This app allows you to add desired items from different online retailers to a watchlist and set your desired price. The app will notify you when the item price drops to the desired level via text notification.

## Authors

Marni Hager, Jae Loney, Pedro Perez, Sergii Ottryshko

## User Stories

<https://python401.atlassian.net/wiki/spaces/US/pages/590051/User+Stories+-+My+Price+Scout>

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

![UML](https://github.com/Cuatro-Programadores/my-price-scout/blob/main/images/my-price-scout-uml.png)

## Wireframe

![Wireframe](https://github.com/Cuatro-Programadores/my-price-scout/blob/main/images/Wireframe-MyPriceScout.png)
