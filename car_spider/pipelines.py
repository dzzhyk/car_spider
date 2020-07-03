# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

from car_spider.items import DetailLinkItem
from car_spider.items import DetailItem
from car_spider.constant import SpiderConstant
import json


# pipeline
class DetailLinkPipeline:

    def __init__(self):
        self.fp_link = open(SpiderConstant.HREF_FILE, "w", encoding='utf-8')
        self.fp_detail = open(SpiderConstant.TARGET_DIR+SpiderConstant.TARGET_FILENAME, "w", encoding='utf-8')

    def process_item(self, item, spider):

        content = json.dumps(dict(item), ensure_ascii=False)
        if isinstance(item, DetailLinkItem):
            self.fp_link.write(content + "\n")
            self.fp_link.flush()
        if isinstance(item, DetailItem):
            self.fp_detail.write(content + "\n")
            self.fp_detail.flush()
        return item

    def close_spider(self, spider):
        self.fp_link.close()
        self.fp_detail.close()
        print("导出link信息结束")
