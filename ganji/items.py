# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class GanjiItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = scrapy.Field()
    price = scrapy.Field()
    house_type = scrapy.Field()
    address = scrapy.Field()
    decorate_degree = scrapy.Field()
    area = scrapy.Field()
    floor = scrapy.Field()
    head_direction = scrapy.Field()
    phone = scrapy.Field()
