# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class CrawlmikanPipeline:
    def process_item(self, item, spider):
        with open('magnet_links.txt', 'a+') as f:
            f.write(item['title'] + '\n')
            f.write(item['magnet_link'] + '\n\n')
