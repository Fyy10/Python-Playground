# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import redis
from itemadapter import ItemAdapter
from .items import ImdbCrawlerItem, ImdbDetailCrawlerItem


# write page links to redis server
def write_redis(redis_obj, item):
    page_link = 'https://www.imdb.com' + item['page_link']
    redis_obj.rpush('imdb:movie_pages', page_link)


class ImdbCrawlerPipeline:
    # create connection pool
    def __init__(self):
        pool = redis.ConnectionPool(host='localhost', port=6379, password='', max_connections=1024)
        coon = redis.Redis(connection_pool=pool)
        self.redis_obj = coon

    def process_item(self, item, spider):
        if isinstance(item, ImdbCrawlerItem):
            write_redis(self.redis_obj, item)
        elif isinstance(item, ImdbDetailCrawlerItem):
            with open('Details.txt', 'a+') as f:
                # split by ','
                data_line = '{}|{}|{}|{}|{}|{}|{}|{}|{}|{}|{}|{}\n'.format(
                    item['title'],
                    item['year'],
                    item['district'],
                    item['length'],
                    item['category'],
                    item['rating'],
                    item['metascore'],
                    item['votes'],
                    item['gross'],
                    item['director'],
                    item['star'],
                    item['review']
                )
                f.write(data_line)
