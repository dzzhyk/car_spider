# -*- coding: utf-8 -*-

# @Time : 2020/7/2 15:01 
# @Author : dzzhyk
# @File : redis_pipelines.py
# @Software: PyCharm


from datetime import datetime


# Redis-Pipelines
#TODO: 暂时不用
class DqdPipeline(object):

    def process_item(self, item, spider):
        item["crawled"] = datetime.utcnow()
        item["spider"] = spider.name
        return item
