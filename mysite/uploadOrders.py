"""
--------------------------
Prior to running, the following commands must be run:

$ python manage.py makemigrations
$ python manage.py migrate 
-----------------------------------------

This adds entries to the database with the data from the 
Test/input_clinics.csv file for testing purposes.

Usage:
    $ python uploadTestData.py


"""
# Need to setup the django enviornment, so the setting module can be located.
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings")
import django
django.setup()

import datetime
from enum import IntEnum
from product.models import Item
from orders.models import Order, OrderedItem

# CSV input file for clinic locations.
PRODUCT_INPUT_FILE = r"Test/input_items.csv"

class InputHeaders(IntEnum):
    NAME = 0
    PRICE = 1
    TOTAL_STOCK = 2
    DESCRIPTION = 3
    PIC_ADDRESS = 4
    CATEGORY = 5

def createItem(data_list):
    item_obj = Item.objects.create(
        name=data_list[InputHeaders.NAME],
        price=data_list[InputHeaders.PRICE],
        total_stock=data_list[InputHeaders.TOTAL_STOCK],
        description=data_list[InputHeaders.DESCRIPTION],
        pic_address=data_list[InputHeaders.PIC_ADDRESS],
        category=data_list[InputHeaders.CATEGORY],
    )

    return item_obj


def main():
    with open(PRODUCT_INPUT_FILE, "r") as fp:
        # Ignore the headers
        fp.readline()
        item = []
        for line in fp:
            data = line.rstrip().split(",")
        
            item.append(createItem(data))

    n = 2
    for i in range(3):
        created_order = Order.objects.create(order_id=i + 1, user_id=i, total_cost=10)
        
        for j in range(3):
            OrderedItem.objects.create(quantity=n, order=created_order, product=item[n])
            n += 1

        if n < 6:
            n = 0


if __name__ == "__main__":
    main()