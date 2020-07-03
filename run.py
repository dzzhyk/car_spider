# -*- coding: utf-8 -*-

# @Time : 2020/7/2 0:32 
# @Author : dzzhyk
# @File : run.py 
# @Software: PyCharm

from scrapy.cmdline import execute
import threading


# execute('scrapy genspider guazi_brand_model www.guazi.com'.split())
# execute('scrapy genspider guazi_info_link www.guazi.com'.split())

# execute('scrapy crawl guazi_brand_model'.split())
# execute('scrapy crawl guazi_info_link'.split())
execute('scrapy crawl guazi_info_link -s LOG_FILE=./log/guazi_info_link.log'.split())


if __name__ == '__main__':
    pass