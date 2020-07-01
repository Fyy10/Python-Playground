# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class CrawllianjiaItem(scrapy.Item):
    # define the fields for your item here like:
    href = scrapy.Field()


class DetailItem(scrapy.Item):
    title = scrapy.Field()
    price = scrapy.Field()
