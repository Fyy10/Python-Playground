# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ImdbCrawlerItem(scrapy.Item):
    # define the fields for your item here like:
    # 电影详情页链接
    page_link = scrapy.Field()


class ImdbDetailCrawlerItem(scrapy.Item):
    # 标题
    title = scrapy.Field()
    # 年份
    year = scrapy.Field()
    # 地区
    district = scrapy.Field()
    # 时长
    length = scrapy.Field()
    # 类别
    category = scrapy.Field()
    # 评分
    rating = scrapy.Field()
    # metascore
    metascore = scrapy.Field()
    # 投票数
    votes = scrapy.Field()
    # 票房
    gross = scrapy.Field()
    # 导演
    director = scrapy.Field()
    # 演员
    star = scrapy.Field()
    # 评论个数
    review = scrapy.Field()
