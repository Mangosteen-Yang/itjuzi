# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class DmozItem(scrapy.Item):
    product = scrapy.Field()
    company = scrapy.Field()
    location = scrapy.Field()
    # website = scrapy.Field()
    hire_urls = scrapy.Field()
