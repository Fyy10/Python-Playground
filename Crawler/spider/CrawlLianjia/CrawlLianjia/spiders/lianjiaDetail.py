import scrapy
from scrapy_redis.spiders import RedisCrawlSpider
from ..items import DetailItem


class LianjiadetailSpider(RedisCrawlSpider):
    name = 'lianjiaDetail'
    allowed_domains = ['cd.lianjia.com']
    redis_key = 'lianjia:hrefs'
    # start_urls = ['http://cd.lianjia.com/']

    def parse(self, response):
        item = DetailItem()
        item['title'] = response.xpath('//div[@class="title"]/h1[@class="main"]/@title').extract_first()
        item['price'] = response.xpath('//span[@class="unitPriceValue"]/text()').extract_first()
        yield item
