# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import redis
from .items import CrawllianjiaItem, DetailItem


def write_redis(redis_obj, item):
    redis_obj.rpush('lianjia:hrefs', item['href'])


class CrawllianjiaPipeline:
    # 初始化redis连接
    def __init__(self):
        # 创建连接池
        pool = redis.ConnectionPool(host='localhost', port=6379, password='', max_connections=1024)
        # 创建连接对象
        coon = redis.Redis(connection_pool=pool)
        self.redis_obj = coon

    def process_item(self, item, spider):
        if isinstance(item, CrawllianjiaItem):
            write_redis(self.redis_obj, item)
        elif isinstance(item, DetailItem):
            with open('Details.txt', 'a+') as f:
                f.write('{} {}\n'.format(item['title'], item['price']))
