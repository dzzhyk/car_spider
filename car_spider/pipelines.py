# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

from car_spider.items import DetailLinkItem
from car_spider.items import DetailItem
import json


# pipeline
class DetailLinkPipeline:

    def __init__(self):
        self.fp_link = open("data/guazi/guazi_link.txt", "w", encoding='utf-8')
        self.fp_detail = open("data/guazi/guazi_detail.txt", "w", encoding='utf-8')

    def process_item(self, item, spider):

        content = json.dumps(dict(item), ensure_ascii=False)
        if isinstance(item, DetailLinkItem):
            self.fp_link.write(content + "\n")
        if isinstance(item, DetailItem):
            self.fp_detail.write(content + "\n")
        return item

    def close_spider(self, spider):
        self.fp_link.close()
        self.fp_detail.close()
        print("导出link信息结束")
