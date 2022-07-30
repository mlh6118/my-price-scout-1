Class inputs/outputs:
* IO Utils
  * Capture email: inputs - email, outputs - validated email 
  * Capture phone: inputs - phone, outputs - validated phone
  * Capture carrier: inputs - carrier, validated carrier
  * Capture url: inputs - url, validated url


* App
  * get_or_create_user: inputs - email, phone, carrier, outputs - User instance
    * helper methods: get_user, create_user, save_user
    * save_user will parse the User instance into key values and save to Db 
      using Database Utils
  * menu: inputs - none, outputs - screen prompts or return information
    * helpers: IO Utils, User, and Item
  * remove_url: calls the remove_url method in Item
    * inputs - website name (i.e., Amazon), outputs - confirmation 
      string
    * if removing the only link, then prompt user for new link or to 
      remove item
  * manage_user_items: logic for when a user has items to add, remove, or 
    edit items


* User
  * add_item: inputs - product name, url(s), target_price(s), output - none
  * remove_item: inputs - product name, output - none 
  * get_items: inputs - none, output - returns user watchlist
  * edit_item: inputs - product name, output - none


* Item - This will act upon the Link class to add, remove, and change url(s).
  * add_url: inputs - url(s), output - confirmation string  (may need to 
    break this out to individual links)
  * add_name: inputs - name, output - confirmation string
  * add_target_price: - inputs - int, output - confirmation string
  * item_url_count: inputs - name, output - int
  * remove_url: inputs - website name (i.e., Amazon), output - confirmation 
    string
  * get_summary: inputs - name, output - all data for the item (representation)
  * change_url: inputs - website name, output - confirmation, calls 
    remove_url followed by add_url
  * is_item_being_tracked: inputs - boolean, output - string about tracking, 
    returns boolean (this should toggle tracking)


* Db Utils
  * get_data: inputs - email as key, outputs - email as key, User as value 
    from database
  * set_data: inputs - email as key, outputs - User as value to database


* Scraper
  * scrape_Amazon: inputs - url, outputs - price
  * scrape_Target: inputs - url, outputs - price
  * scrape_Walmart: inputs - url, outputs - price


* Tracker
  * fetch_data: inputs - none, outputs - refreshed data for item 
  * send_notification: inputs - price, email, outputs - text notification


* Link
  * website is the name (i.e., Amazon, Target, Walmart)
  * url is the specific webpage the user puts in
  * actual_price is the value found on the link by the Scraper