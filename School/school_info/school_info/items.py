# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.item import Item, Field
class FaultyItem(scrapy.Item):
    email = scrapy.Field()
    name = scrapy.Field()
    phone = scrapy.Field()
    college = scrapy.Field()
    profession = scrapy.Field()
    # title = scrapy.Field()
    link = scrapy.Field()
    # img = scrapy.Field()
    # background = scrapy.Field()
    # location = scrapy.Field()

