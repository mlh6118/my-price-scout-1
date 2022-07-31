import pytest

from files.user import User


def test_get_item():
    user = User("mock email", "mock phone number" , "mock cell carrier")
    mock_item = {"name": "tv"}
    user.watchlist.append(mock_item)

    item = user.get_item("tv")

    assert item == mock_item




# def test_add_item():
#     user = User("mock email", "mock phone number" , "mock cell carrier")
#     item = "item"
#     assert len(user.watchlist) == 0
    
#     user.add_item(item)
    
#     assert len(user.watchlist) == 1 
#     assert user.watchlist[0] == item

