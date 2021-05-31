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
from product.models import Item, Size

# CSV input file for clinic locations.
PRODUCT_INPUT_FILE = r"Test/input_items.csv"


class InputHeaders(IntEnum):
    NAME = 0
    PRICE = 1
    TOTAL_STOCK = 2
    DESCRIPTION = 3
    PIC_ADDRESS = 4
    CATEGORY = 5
    SIZE = 6
    SMALL_SIZE = 7
    MEDIUM_SIZE = 8
    LARGE_SIZE = 9


def createItem(data_list):
    item_obj = Item.objects.create(
        name=data_list[InputHeaders.NAME],
        price=data_list[InputHeaders.PRICE],
        # total_stock=data_list[InputHeaders.TOTAL_STOCK],
        description=data_list[InputHeaders.DESCRIPTION],
        pic_address=data_list[InputHeaders.PIC_ADDRESS],
        category=data_list[InputHeaders.CATEGORY],
    )

    return item_obj


def main():
    with open(PRODUCT_INPUT_FILE, "r") as fp:
        # Ignore the headers
        fp.readline()

        for line in fp:
            data = line.rstrip().split(",")

            item = createItem(data)

            size_types = data[InputHeaders.SIZE].split(" ")

            for size_type in size_types:
                if size_type == 'small':
                    Size.objects.create(product=item, stock=data[InputHeaders.SMALL_SIZE],
                                        size_type='small')
                if size_type == 'medium':
                    Size.objects.create(product=item, stock=data[InputHeaders.MEDIUM_SIZE],
                                        size_type='medium')
                if size_type == 'large':
                    Size.objects.create(product=item, stock=data[InputHeaders.LARGE_SIZE],
                                        size_type='large')


if __name__ == "__main__":
    main()
