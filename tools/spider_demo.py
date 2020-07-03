# -*- coding: utf-8 -*-

# @Time : 2020/7/2 1:42 
# @Author : dzzhyk
# @File : spider_demo.py
# @Software: PyCharm

import requests

# 测试

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US) AppleWebKit/532.9 (KHTML, like Gecko) Chrome/5.0.310.0 Safari/532.9',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'accept-language': 'zh-CN,zh;q=0.9,und;q=0.8,zh-TW;q=0.7',
    # 'cookie': 'antipas=7589738TL249R0692497Pu302644;uuid=fbd7c78b-48fc-4708-965a-0b45e7a34361;ganji_uuid=9143531327448859110537;lg=1;close_finance_popup=2020-07-02;cityDomain=anji;clueSourceCode=%2A%2300;user_city_id=120;sessionid=6e4d4f7a-d7f9-420e-be87-689467dfa316;Hm_lvt_936a6d5df3f3d309bda39e92da3dd52f=1593614525,1593624914;cainfo=%7B%22ca_a%22%3A%22-%22%2C%22ca_b%22%3A%22-%22%2C%22ca_s%22%3A%22seo_baidu%22%2C%22ca_n%22%3A%22default%22%2C%22ca_medium%22%3A%22-%22%2C%22ca_term%22%3A%22-%22%2C%22ca_content%22%3A%22-%22%2C%22ca_campaign%22%3A%22-%22%2C%22ca_kw%22%3A%22-%22%2C%22ca_i%22%3A%22-%22%2C%22scode%22%3A%22-%22%2C%22keyword%22%3A%22-%22%2C%22ca_keywordid%22%3A%22-%22%2C%22display_finance_flag%22%3A%22-%22%2C%22platform%22%3A%221%22%2C%22version%22%3A1%2C%22client_ab%22%3A%22-%22%2C%22guid%22%3A%22fbd7c78b-48fc-4708-965a-0b45e7a34361%22%2C%22ca_city%22%3A%22cq%22%2C%22sessionid%22%3A%226e4d4f7a-d7f9-420e-be87-689467dfa316%22%7D;preTime=%7B%22last%22%3A1593624947%2C%22this%22%3A1593614524%2C%22pre%22%3A1593614524%7D;Hm_lpvt_936a6d5df3f3d309bda39e92da3dd52f=1593624948;'
}


def get_detail():
    url = "http://www.guazi.com/wei/dazhong"
    resp = requests.get(url, headers=headers)
    text = resp.content.decode('utf-8')
    print(text)


if __name__ == '__main__':
    get_detail()