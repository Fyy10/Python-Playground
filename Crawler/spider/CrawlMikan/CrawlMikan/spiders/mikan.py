import scrapy
from ..items import CrawlmikanItem


class MikanSpider(scrapy.Spider):
    name = 'mikan'
    allowed_domains = ['mikanani.me']
    start_urls = ['https://mikanani.me/Home/Classic']

    def parse(self, response):
        links = response.xpath('//tbody/tr')
        for link in links:
            item = CrawlmikanItem()
            item['magnet_link'] = link.xpath('./td/a/@data-clipboard-text').extract_first()
            yield item
