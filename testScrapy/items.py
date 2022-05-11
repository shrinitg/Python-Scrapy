# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.item import Item, Field


class TestscrapyItem(Item):
    # title = Field()
    # link = Field()

    # product_name = scrapy.Field()
    # product_sale_price = scrapy.Field()
    # product_sale_currency = scrapy.Field()
    # product_original_price = scrapy.Field()
    # product_brand = scrapy.Field()
    # product_image_url = scrapy.Field()
    # product_discount_pert = scrapy.Field()

    product_title = scrapy.Field()
    product_handle = scrapy.Field()
    product_description = scrapy.Field()
    product_price = scrapy.Field()
