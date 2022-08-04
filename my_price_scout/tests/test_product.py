import pytest

# print('__file__={0:<35} | __name__={1:25} | __package__={2:<25}'.format(
#     __file__,__name__,str(__package__)))


from ..my_price_scout_files.product import Product2


def test_exists():
    assert Product2.product_test()
