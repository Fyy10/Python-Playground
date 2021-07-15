import scrapy
from scrapy_redis.spiders import RedisCrawlSpider
from ..items import ImdbCrawlerItem


class ImdbSpider(RedisCrawlSpider):
    name = 'imdb'
    allowed_domains = ['imdb.com']
    redis_key = 'imdb:start_pages'
    # start_urls = ['http://imdb.com/']

    def parse(self, response):
        page_list = response.xpath('//div[@class="lister-item-content"]')
        for page in page_list:
            item = ImdbCrawlerItem()
            item['page_link'] = page.xpath('./h3/a/@href').extract_first()
            yield item
