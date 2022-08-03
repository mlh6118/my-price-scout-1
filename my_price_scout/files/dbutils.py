import dotenv
import os
from pymongo import MongoClient
from bson.json_util import dumps, loads
from user import User
from product import Product
from specific_product import Specific_Product


dotenv.load_dotenv(dotenv.find_dotenv())


password = os.environ.get("MONGO_PASSWORD")


class DBUtils():
    def __init__(self):
        self.connection = MongoClient(
            f"mongodb+srv://mypricescout:{password}@my-price-scout-users.yugh3.mongodb.net/?retryWrites=true&w=majority")

    def set_user(self, user):

        found_user = self.connection.user_data.user_data.find_one(
            {"email": f"{user.email}"})
        if found_user:
            self.connection.user_data.user_data.delete_one(
                {"email": f"{user.email}"})

        user_document = {
            "email": f"{user.email}",
            "phone_number": user.phone_number,
            "cell_carrier": f"{user.cell_carrier}",
            "watchlist": [{"name": product.product_name, "is_product_being_tracked": product.is_product_being_tracked, "specific_product_list": [{"website": f"{specific_product.website}", "url": f"{specific_product.url}", "price": f"{specific_product.price}"} for specific_product in product.specific_product_list], "target_price": f"{product.target_price}"} for product in user.watchlist]
        }

        self.connection.user_data.user_data.insert_one(user_document)

    def get_user(self, user_name):

        found_user = self.connection.user_data.user_data.find_one(
            {"email": f"{user_name}"})
        if found_user:
            parsed_user = User(found_user["email"], found_user["phone_number"], found_user["cell_carrier"], [Product(item["name"], item["target_price"], [
                Specific_Product(link["website"], link["url"], link["price"]) for link in item["specific_product_list"]]) for item in found_user["watchlist"]])

            return parsed_user

        else:

            return None

    def get_all_users(self):

        retrieved_users_cursor = self.connection.user_data.user_data.find({})
        user_list_cursor = list(retrieved_users_cursor)
        json_user_list = dumps(user_list_cursor)
        user_list = loads(json_user_list)

        return user_list

    def update_all_users(self):
        user_list = self.get_all_users()

        for user in user_list:
            for product in user["watchlist"]:
                # target_price = product["target_price"]
                for specific_product in product["specific_product_list"]:
                    # if specific_product["website"] == "Amazon":
                    #     specific_product["price"] = scraper.scrape_amazon()
                    # if specific_product["website"] == "Target":
                    #     specific_product["price"] = scraper.scrape_target()
                    # if specific_product["website"] == "Walmart":
                    #     specific_product["price"] = scraper.scrape_walmart()
                    specific_product["price"] = 555

        return user_list

    def update_and_save_users_to_db(self):

        updated_user_list = self.update_all_users()
        if updated_user_list:
            self.connection.user_data.user_data.delete_many({})
            self.connection.user_data.user_data.insert_many(updated_user_list)


if __name__ == "__main__":
    db = DBUtils()
    db.update_and_save_users_to_db()
