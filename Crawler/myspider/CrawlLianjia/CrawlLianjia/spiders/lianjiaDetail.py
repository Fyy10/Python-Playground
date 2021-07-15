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
        item['area'] = response.xpath('//div[@class="areaName"]/span[@class="info"]/a[1]/text()').extract_first()
        item['price'] = response.xpath('//span[@class="unitPriceValue"]/text()').extract_first()
        yield item
