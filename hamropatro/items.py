# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class HamropatroItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    eng = scrapy.Field()
    nep = scrapy.Field()
    tithi = scrapy.Field()
    events = scrapy.Field()
