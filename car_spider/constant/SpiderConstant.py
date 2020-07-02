# -*- coding: utf-8 -*-

# @Time : 2020/7/2 19:35 
# @Author : dzzhyk
# @File : SpiderConstant.py 
# @Software: PyCharm

# 常量定义

# 该guazi_info_link.py的目标href集成页面文件位置
HREF_FILE = "data/guazi/devided/guazi_href_part_1"

# 生成目标目录和生成目标文件
TARGET_DIR = ""
TARGET_FILENAME = ""

# 一些参数设置
BOT_NAME = 'car_spider'

ROBOTSTXT_OBEY = False

CONCURRENT_REQUESTS = 10
DOWNLOAD_DELAY = 3

COOKIES_ENABLED = False

DEFAULT_REQUEST_HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'accept-language': 'zh-CN,zh;q=0.9,und;q=0.8,zh-TW;q=0.7',
    'cookie': 'antipas=3236N504516y8F89277621826;uuid=fbd7c78b-48fc-4708-965a-0b45e7a34361;ganji_uuid=9143531327448859110537;lg=1;close_finance_popup=2020-07-02;cityDomain=anji;clueSourceCode=%2A%2300;user_city_id=120;sessionid=6e4d4f7a-d7f9-420e-be87-689467dfa316;Hm_lvt_936a6d5df3f3d309bda39e92da3dd52f=1593614525,1593624914;cainfo=%7B%22ca_a%22%3A%22-%22%2C%22ca_b%22%3A%22-%22%2C%22ca_s%22%3A%22seo_baidu%22%2C%22ca_n%22%3A%22default%22%2C%22ca_medium%22%3A%22-%22%2C%22ca_term%22%3A%22-%22%2C%22ca_content%22%3A%22-%22%2C%22ca_campaign%22%3A%22-%22%2C%22ca_kw%22%3A%22-%22%2C%22ca_i%22%3A%22-%22%2C%22scode%22%3A%22-%22%2C%22keyword%22%3A%22-%22%2C%22ca_keywordid%22%3A%22-%22%2C%22display_finance_flag%22%3A%22-%22%2C%22platform%22%3A%221%22%2C%22version%22%3A1%2C%22client_ab%22%3A%22-%22%2C%22guid%22%3A%22fbd7c78b-48fc-4708-965a-0b45e7a34361%22%2C%22ca_city%22%3A%22cq%22%2C%22sessionid%22%3A%226e4d4f7a-d7f9-420e-be87-689467dfa316%22%7D;preTime=%7B%22last%22%3A1593624947%2C%22this%22%3A1593614524%2C%22pre%22%3A1593614524%7D;Hm_lpvt_936a6d5df3f3d309bda39e92da3dd52f=1593624948;'
}

SPIDER_MIDDLEWARES = {
   'car_spider.middlewares.MyUserAgentMiddleware': 543
}

ITEM_PIPELINES = {
   'car_spider.pipelines.DetailLinkPipeline': 300
}

AUTOTHROTTLE_MAX_DELAY = 60

AUTOTHROTTLE_DEBUG = True