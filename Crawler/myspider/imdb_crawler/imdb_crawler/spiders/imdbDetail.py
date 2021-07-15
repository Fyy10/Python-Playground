import scrapy
from scrapy_redis.spiders import RedisCrawlSpider
from ..items import ImdbDetailCrawlerItem


class ImdbdetailSpider(RedisCrawlSpider):
    name = 'imdbDetail'
    allowed_domains = ['imdb.com']
    redis_key = 'imdb:movie_pages'
    # start_urls = ['http://imdb.com/']

    def parse(self, response):
        item = ImdbDetailCrawlerItem()
        title_wrapper = response.xpath('//div[@class="title_wrapper"]')

        # item data
        item['title'] = title_wrapper.xpath('./h1/text()').extract_first()[:-1]
        item['year'] = title_wrapper.xpath('./h1/span[@id="titleYear"]/a/text()').extract_first()
        item['district'] = response.xpath('//div[@id="titleDetails"]/div[2]/a/text()').extract_first()
        # cal length: [hour, min]
        hh_mm = title_wrapper.xpath('./div/time/text()').extract_first().split()
        if len(hh_mm) == 2:
            item['length'] = '{} {}'.format(hh_mm[0], hh_mm[1])
        else:
            item['length'] = hh_mm[0]
        # category
        # the last one is date, ignore it
        categories = title_wrapper.xpath('./div/a/text()').extract()[:-1]
        item['category'] = ''
        for cat in categories:
            item['category'] = item['category'] + cat + ' '
        # remove the last ' '
        item['category'] = item['category'][:-1]
        item['rating'] = response.xpath('//div[@class="ratings_wrapper"]//span[@itemprop="ratingValue"]/text()').extract_first()
        item['metascore'] = response.xpath('//div[@class="titleReviewBar "]/div/a/div/span/text()').extract_first()
        item['votes'] = response.xpath('//div[@class="ratings_wrapper"]//span[@itemprop="ratingCount"]/text()').extract_first().replace(',', '')
        item['gross'] = response.xpath('//div[@id="titleDetails"]//div/h4[contains(text(), "Gross")]/../text()').extract()[1].split()[0][1:].replace(',', '')
        # directors
        directors = response.xpath('//div[@class="plot_summary "]/div[2]/a/text()').extract()
        item['director'] = ''
        for dt in directors:
            item['director'] = item['director'] + dt + '+'
        # remove the last '+'
        item['director'] = item['director'][:-1]
        # stars
        stars = response.xpath('//div[@class="plot_summary "]/div[4]/a/text()').extract()[:-1]
        item['star'] = ''
        for star in stars:
            item['star'] = item['star'] + star + '+'
        # remove the las '+'
        item['star'] = item['star'][:-1]
        item['review'] = response.xpath('//div[@class="titleReviewBar "]/div/div/span[@class="subText"]/a/text()').extract_first().split(' ')[0].replace(',', '')
        yield item
