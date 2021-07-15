import scrapy
from scrapy_redis.spiders import RedisCrawlSpider
from ..items import CrawllianjiaItem


class LianjiaSpider(RedisCrawlSpider):
    name = 'lianjia'
    allowed_domains = ['cd.lianjia.com']
    redis_key = 'lianjia:start_urls'
    # start_urls = ['http://cd.lianjia.com/']

    def parse(self, response):
        li_list = response.xpath('//ul[@class="sellListContent"]/li')
        for li in li_list:
            item = CrawllianjiaItem()
            item['href'] = li.xpath('./a/@href').extract_first()
            yield item
