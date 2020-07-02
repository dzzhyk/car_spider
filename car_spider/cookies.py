# -*- coding: utf-8 -*-

# @Time : 2020/7/2 16:00 
# @Author : dzzhyk
# @File : cookies.py 
# @Software: PyCharm

import requests
import json
import redis
import logging
from car_spider.car_spider.settings import REDIS_URL

logger = logging.getLogger(__name__)

##使用REDIS_URL链接Redis数据库, deconde_responses=True这个参数必须要，数据会变成byte形式 完全没法用
reds = redis.Redis.from_url(REDIS_URL, db=2, decode_responses=True)
login_url = 'https://www.guazi.com'


##获取Cookie
def get_cookie():
    s = requests.Session()
    response = s.get(login_url)
    cookies = response.cookies.get_dict()
    logger.warning("获取Cookie成功")
    return json.dumps(cookies)


if __name__ == '__main__':
    print(get_cookie())